// Ported from echo/frontend/helperJS/vortex.js (createVortexParticle,
// renderVortex) by way of MuseLab/frontend/src/lib/imprint/vortexCanvas.ts
// (mountImprintVortex) — this module keeps MuseLab's already-adapted
// constants (angle step 0.48, not Echo's original 0.42) since that's the
// precedent this project inherits from, not a fresh derivation.
//
// Usage:
//   import { mountVortexField } from '../../assets/js/vortex-field.js';
//   const handle = mountVortexField(containerEl, [
//     { text: 'TypeScript', score: 1.0, core: true },
//     { text: 'Python', score: 0.6 },
//   ], { motion: 0.28, intensity: 0.34 });
//   // handle.destroy() to tear down

import { readTokens, withAlpha } from './theme-colors.js';

function vortexParams(motion, intensity) {
  return {
    motionScale: 2 + motion * 14,
    wobbleAmount: 2 + intensity * 18,
    wobbleRate: 0.005 + intensity * 0.016,
    depthScale: 0.06 + intensity * 0.2,
    spiralSpacing: 4 + intensity * 6,
    vortexSpeed: 3 + motion * 10,
    outerSpread: 28 + intensity * 42,
    intensity,
  };
}

function spawnParticle(term, index, params) {
  const isCore = Boolean(term.core);
  const semanticScore = Math.min(1, term.score ?? 0.4);
  const spiralStep = params.spiralSpacing + params.intensity * 2;
  return {
    text: term.text,
    core: isCore,
    semanticScore,
    angle: index * 0.48,
    radius: 16 + index * spiralStep + (1 - semanticScore) * params.outerSpread,
    z: Math.sin(index * 0.65) * params.intensity * 90,
    size: isCore ? Math.min(30, 15 + semanticScore * 14) : Math.min(19, 11 + semanticScore * 8),
    speed: 0.0012 + (1 - semanticScore) * 0.0018 + Math.random() * 0.0008,
    opacity: isCore ? 0.9 : 0.24 + semanticScore * 0.4,
    wobbleSeed: Math.random() * Math.PI * 2,
  };
}

export function mountVortexField(container, terms, opts = {}) {
  const motion = opts.motion ?? 0.28;
  const intensity = opts.intensity ?? 0.34;
  const interactive = opts.interactive ?? true;
  const reduceMotion = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;

  const params = vortexParams(motion, intensity);
  const particles = terms.map((t, i) => spawnParticle(t, i, params));

  const canvas = document.createElement('canvas');
  container.appendChild(canvas);
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  let width, height, fitScale;

  function fit() {
    const rect = container.getBoundingClientRect();
    width = Math.max(1, Math.round(rect.width));
    height = Math.max(1, Math.round(rect.height));
    canvas.width = Math.max(1, Math.round(width * dpr));
    canvas.height = Math.max(1, Math.round(height * dpr));
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    fitScale = Math.min(width, height) / (opts.referenceSize ?? 420);
  }
  fit();
  const ro = new ResizeObserver(fit);
  ro.observe(container);

  let time = 0;
  let raf = null;
  const view = { rotation: opts.initialRotation ?? -0.3, tilt: 0, scale: 1, targetScale: 1, offsetX: 0, offsetY: 0, targetOffsetX: 0, targetOffsetY: 0 };
  const drag = { active: false, lastX: 0, lastY: 0 };

  function draw() {
    const theme = readTokens();
    ctx.clearRect(0, 0, width, height);
    const cx = (opts.centerX ?? 0.5) * width;
    const cy = (opts.centerY ?? 0.5) * height;
    ctx.save();
    ctx.translate(cx + view.offsetX, cy + view.offsetY);
    ctx.scale(view.scale, view.scale);
    ctx.rotate(view.rotation);
    ctx.scale(1, 0.92 + view.tilt * 0.08);

    ctx.beginPath();
    ctx.arc(0, 0, 2, 0, Math.PI * 2);
    ctx.fillStyle = withAlpha(theme.accent, 0.55);
    ctx.fill();

    for (let i = 0; i < particles.length; i++) {
      const p = particles[i];
      const a = p.angle + time * p.speed * params.motionScale * params.vortexSpeed * 0.00135;
      const spiral = p.radius + Math.sin(time * params.wobbleRate + p.wobbleSeed + i * 0.4) * params.wobbleAmount;
      const x = Math.cos(a) * spiral * fitScale;
      const y = (Math.sin(a) * spiral * 0.62 + p.z * params.depthScale) * fitScale;

      ctx.font = `${p.core ? 500 : 400} ${p.size}px "Cormorant Garamond", Georgia, serif`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillStyle = withAlpha(p.core ? theme.ink : theme.muted, p.opacity * (p.core ? 1 : 0.7));
      ctx.fillText(p.text, x, y);
    }
    ctx.restore();
  }

  function loop() {
    view.scale += (view.targetScale - view.scale) * 0.12;
    view.offsetX += (view.targetOffsetX - view.offsetX) * 0.12;
    view.offsetY += (view.targetOffsetY - view.offsetY) * 0.12;
    if (!drag.active && opts.ambientDrift !== false) view.rotation += 0.00028;
    time += 1;
    draw();
    raf = requestAnimationFrame(loop);
  }

  let onDown, onMove, onUp;
  if (reduceMotion) {
    draw();
  } else {
    loop();
    if (interactive) {
      onDown = (e) => { drag.active = true; drag.lastX = e.clientX; drag.lastY = e.clientY; container.classList.add('is-dragging'); container.setPointerCapture?.(e.pointerId); };
      onMove = (e) => { if (!drag.active) return; view.rotation += (e.clientX - drag.lastX) * 0.005; view.tilt = Math.max(-1, Math.min(1, view.tilt + (e.clientY - drag.lastY) * 0.003)); drag.lastX = e.clientX; drag.lastY = e.clientY; };
      onUp = (e) => { drag.active = false; container.classList.remove('is-dragging'); if (container.hasPointerCapture?.(e.pointerId)) container.releasePointerCapture(e.pointerId); };
      container.addEventListener('pointerdown', onDown);
      container.addEventListener('pointermove', onMove);
      container.addEventListener('pointerup', onUp);
      container.addEventListener('pointercancel', onUp);
    }
  }

  return {
    destroy() {
      if (raf) cancelAnimationFrame(raf);
      ro.disconnect();
      if (onDown) {
        container.removeEventListener('pointerdown', onDown);
        container.removeEventListener('pointermove', onMove);
        container.removeEventListener('pointerup', onUp);
        container.removeEventListener('pointercancel', onUp);
      }
      canvas.remove();
    },
  };
}
