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
parser = argparse.ArgumentParser(description="Render privacy-safe device captures as Hub media")
parser.add_argument("--home", required=True, help="JSON framebuffer recording of the synthetic HOME cover")
parser.add_argument("--relative", required=True, help="JSON recording of the relative-latency device demo")
parser.add_argument("--raw", default="/tmp/networkmonitor-cover.rgb", help="Raw RGB output for ffmpeg")
args = parser.parse_args()
home = json.loads(Path(args.home).read_text())
relative = json.loads(Path(args.relative).read_text())
def nearest(frames, t):
 return min(frames, key=lambda f: abs(f["t"] - t))
for name, t in [("flat", 1.5), ("jitter", 5.5), ("spikes", 9.5)]:
 png("docs/media/graph-relative-" + name + "-device.png", nearest(relative, t))
png("docs/media/networkmonitor-cover-home.png", nearest(home, .8))
png("docs/media/networkmonitor-cover-history.png", nearest(relative, 9.5))
selected = [nearest(home, .04 + i * .1) for i in range(18)]
selected += [nearest(relative, 8.15 + i * .1) for i in range(22)]
Path(args.raw).write_bytes(b"".join(render(f) for f in selected))
print("Prepared 40 frames at 1040x320 for a four-second cover.")

demo = [nearest(home, i * .1) for i in range(18)]
for start in [.2, 4.2, 8.2]:
 demo += [nearest(relative, start + i * .1) for i in range(30)]
Path(args.raw + ".demo").write_bytes(b"".join(render(f) for f in demo))
