// Render the slide-deck figure SVGs to PNG for insertion into the decks.
//
// Usage:
//   NODE_PATH=/Users/renzheng/.workbuddy/binaries/node/workspace/node_modules \
//   node figures/render.js
//
// Two fonts, on purpose: Arial carries the English, Hiragino Sans GB carries
// the Chinese. This machine has no PingFang (the textbook's render.js still
// names it), and a renderer that cannot find a CJK font drops the Chinese and
// leaves empty boxes -- silently, with the English still perfect.
const fs = require('fs');
const path = require('path');
const { Resvg } = require('@resvg/resvg-js');

const svgDir = path.join(__dirname, 'svg');
const outDir = path.join(__dirname, 'png');
fs.mkdirSync(outDir, { recursive: true });

const FONTS = [
  '/System/Library/Fonts/Supplemental/Arial.ttf',
  '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
  '/System/Library/Fonts/Supplemental/Arial Italic.ttf',
  '/System/Library/Fonts/Hiragino Sans GB.ttc',
];

const only = process.argv[2];

for (const f of fs.readdirSync(svgDir).filter((f) => f.endsWith('.svg'))) {
  if (only && !f.includes(only)) continue;
  const svg = fs.readFileSync(path.join(svgDir, f), 'utf8');
  const resvg = new Resvg(svg, {
    fitTo: { mode: 'width', value: 1920 },
    font: { fontFiles: FONTS, loadSystemFonts: false, defaultFontFamily: 'Arial' },
  });
  const png = resvg.render().asPng();
  const out = path.join(outDir, f.replace(/\.svg$/, '.png'));
  fs.writeFileSync(out, png);
  console.log('rendered:', path.basename(out), (png.length / 1024).toFixed(0) + ' KB');
}
