# Profile visual design

The current direction is tactile 3D with subtle Frieren references: a floating silver-and-glass grimoire, lavender light, generous space and animated project cards. Both light and dark GitHub themes are supported. SVG animations stop when reduced motion is requested. The GitHub page uses self-contained images rather than JavaScript.

Reference supplied by the user: https://vc.ru/design/2059945-3d-v-veb-dizajne-2025 (reviewed 2026-09-10).

## Assets

- `assets/grimoire-3d.png`: original transparent illustration generated with the built-in image generation tool.
- `scripts/build-profile-assets.py`: reproducible SVG composition, animation and project card layouts. Run with Python 3 from any directory. The PNG is embedded unchanged so GitHub does not need external SVG image requests.
- `assets/header-{dark,light}.svg` and `assets/project-*-{dark,light}.svg`: generated assets referenced by README.

The snake and contribution-map workflows are independent of these assets. The WakaTime workflow remains disabled. No additional GitHub authorization is needed to publish these visual assets.

## Original image generation prompt

Use case: stylized-concept. Create one premium 3D website hero illustration asset on a genuinely transparent background, square 1024x1024. Subject: a floating enchanted grimoire inspired by Frieren, with pearlescent ivory hardcovers, brushed silver corner fittings, lavender glass page edges and a small glowing four-point star inset in the cover. The book is partly open in a graceful three-quarter perspective, pages gently fanned. A beautiful translucent lavender glass orbital ring curves around and behind the book, tilted diagonally in three dimensions; two small polished chrome spheres and one tiny glass crystal float near it. A delicate blue-violet flower detail evokes Frieren's quiet magical atmosphere. Sophisticated futuristic fantasy, restrained and luxurious, tactile minimal 3D web design, high-end Cinema 4D / Octane product render, real thickness, glass refraction, glossy specular highlights, soft violet rim lighting, gentle ambient occlusion, sculptural silhouette. Strong depth and volume, beautifully lit materials, centered isolated composition with generous safe margin around entire object. No text, no letters, no labels, no logos, no watermark, no ground plane, no rectangular background, no UI, no flat vector drawing. Must be a reusable clean transparent PNG cutout for placement on an animated GitHub profile header.

## Professional portfolio refresh — 2026-09-11

The owner selected **Data Scientist / ML Engineer** as the primary role and
**loxterpoi@gmail.com** as the shared contact for the profile and website.
The header is now shorter, with a clear professional role, restrained typography,
and original vector blue flowers alongside the animated grimoire. Project cards,
contribution animation, light/dark variants and reduced-motion handling remain.

The README now includes professional context, project architectures and source
links, grouped skills, other experiments, and research results with methodology
and limitations. D-MeZO-N figures describe **v2 = combo**, not the original variant.
MITS figures use the 209-problem Q4_K_M/self-consistency evaluation, not the
separate BF16 ladder. Sources are linked next to the claims; no experiments were
rerun for this presentation update. No dates of employment, seniority, business
impact or formal publications have been inferred.

Content source notes are mirrored in the website repository's
[`docs/content.md`](https://github.com/Siesher/Siesher.github.io/blob/main/docs/content.md).
