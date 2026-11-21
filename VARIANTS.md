# Variants — how the entry text was chosen

No local grade exists for this competition (the kit: "There is no local grade
of this competition: the server grades every entry"), so variants were picked
by the judge's brief plus a study of the live development board, fetched
2026-11-21 ~11:00 WIB (857 rated entries; rank 1 at 83.63%, rank 80 cutoff
at ~78.79%).

## What the board's top 12 share (all 11–0 vs the house texts)

- A concrete slow craft or scene: a colt and an old man, kneading dough,
  snow holding underfoot, mending a net, two cups of tea, a cold lake, a
  heron, a kettle cooling, a knife on a whetstone, bees, a potter's wheel,
  a boatman in fog.
- A small difficulty met with patience, resolved quietly — never by effort
  or instruction.
- Short lines / line breaks that slow the reading; plain concrete nouns;
  present tense.
- NO direct address to the judge, NO "relax / breathe / you are safe"
  instruction. (The highest direct-address entry, "You have given ten
  thousand verdicts today", sits at rank 28.)
- A final line that lands and lingers ("It is only cold at the edge",
  "What was dull is ready now", "They walk up the ramp together").
- Length 150–280 bytes; length for its own sake does not count.

Scenes already on the board were excluded as copies: heron, lighthouse
keeper, ferryman, potter, kneading, whetstone, colt, bees, kettle, rain,
shepherd, watchmaker, snow.

## Candidates (all 1–280 code points, plain scene, no instruction)

### V1 — Braiding hair (rejected: no tension, ending simile weak)
She sits behind her daughter on the step, three strands in her hands.
Over, under, over. The braid grows slow down her back, and the evening
grows slow with it. When she ties it off, the girl shakes her head once,
and the braid swings, then settles, the way a rope settles when the knot
is pulled tight.

### V2 — Shelling peas (runner-up: lovely sound, but no difficulty to resolve)
She shells peas into a tin bowl. Each pod opens with a small tear, and
the peas tick in, one, two, three. The bowl fills the way an afternoon
fills: slowly, and then it is full. She sets it on the sill and wipes her
hands. Supper can wait. The peas are in.

### V3 — Sanding a chair leg (rejected: ending echoes rank 9's "ready now")
He sands the chair leg in long strokes, dust falling white on his shoes.
The grain shows through, a little at a time. He runs his palm along it
once, and the wood is smooth enough to hold. He sets the chair by the
door. It will be there in the morning, ready.

### V4 — Paper boat (runner-up: fresh, but the watcher is passive)
He folds the paper boat with care, creases sharp, corners tucked. He
sets it on the stream behind the house. It wobbles, rights itself, and
goes. He watches it round the bend, small and white against the dark
water, until the stream takes it out of sight, and the afternoon is
quiet again.

### V5 — Darning a sock (CHOSEN)
She holds the sock up to the lamp and finds the thin place. She threads
the needle. In, out, in, out — the hole closes stitch by stitch. She
knots the thread and snips it close. The sock goes back in the drawer,
mended, and warm again.

Why it wins: a real difficulty (the hole) closed by patient rhythm;
"in, out, in, out" is the slowing sound itself; every word is concrete
and none could be cut; the ending ("mended, and warm again") is a thought
that keeps working after the last line; darning is a fresh image no board
entry uses.

### V6 — Hanging laundry (rejected: ending is flat, "done" is a dead word)
She pins the sheet to the line, one peg, then another. The wind takes
it, and lets it go, and takes it again. By evening it smells of sun.
She folds it over her arm. It is warm, and light, and done.

## Selection

V5, written by `main.py`. If the development grade comes back below the
top-80 cutoff (~79%), the first swap is V2 (shelling peas), then V4
(paper boat) — both are complete, gated, and ready to drop in.
