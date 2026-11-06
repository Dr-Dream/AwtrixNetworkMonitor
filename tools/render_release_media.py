import json,struct,zlib
from pathlib import Path

w=52;h=16;cell=20;bg=bytes((4,6,9));off=bytes((17,21,27))
def render(f):
 p=f['pixels'];rows=[];blank=bg*w*cell
 for y in range(h):
  row=[]
  for x in range(w):
   c=p[y*w+x];color=bytes(((c>>16)&255,(c>>8)&255,c&255)) if c else off
   row.append(bg*2+color*16+bg*2)
  lit=b''.join(row);rows.extend([blank]*2+[lit]*16+[blank]*2)
 return b''.join(rows)
def png(path,f):
 data=render(f);ww=w*cell;hh=h*cell
 def ch(t,b):return struct.pack('!I',len(b))+t+b+struct.pack('!I',zlib.crc32(t+b)&0xffffffff)
 scan=b''.join(b'\0'+data[y*ww*3:(y+1)*ww*3] for y in range(hh))
 Path(path).write_bytes(b'\x89PNG\r\n\x1a\n'+ch(b'IHDR',struct.pack('!2I5B',ww,hh,8,2,0,0,0))+ch(b'IDAT',zlib.compress(scan))+ch(b'IEND',b''))

import argparse
parser = argparse.ArgumentParser(description="Render synthetic TC002 release captures")
parser.add_argument("capture", help="Local privacy-safe framebuffer JSON recording")
parser.add_argument("--raw", default="/tmp/networkmonitor-release")
args = parser.parse_args()
frames = json.loads(Path(args.capture).read_text())
def near(icon, t):
 return min((f for f in frames if f["icon"] == icon), key=lambda f: abs(f["t"] - t))
for icon in ("false", "true"):
 suffix = "-with-icon" if icon == "true" else ""
 for name, t in [("home", .8), ("alerts", 3.2), ("nodes-tcp", 8.5), ("nodes-http", 9.5)]:
  png("docs/media/" + name + suffix + ".png", near(icon, t))
png("docs/media/networkmonitor-cover-home.png", near("false", .8))
png("docs/media/networkmonitor-cover-history.png", near("false", 8.5))
png("docs/media/networkmonitor-cover-alerts.png", near("false", 3.2))
cover = [near("false", .3 + i * .1) for i in range(12)]
cover += [near("false", 2.5 + i * .1) for i in range(12)]
cover += [near("false", 8.15 + i * .1) for i in range(16)]
Path(args.raw + "-cover.rgb").write_bytes(b"".join(render(f) for f in cover))
demo = [near(icon, .1 + i * .1) for icon in ("false", "true") for i in range(118)]
Path(args.raw + "-demo.rgb").write_bytes(b"".join(render(f) for f in demo))
