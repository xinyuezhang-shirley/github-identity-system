// Settle-in scroll reveal — Motion DNA strand 05 applied to page structure
// itself (exponential-style ease, decelerate-only, no bounce). Add class
// "reveal" to any element; it fades/rises into place once, on first
// intersection, staggered by DOM order.

export function initReveal(selector = '.reveal') {
  const els = document.querySelectorAll(selector);
  if (!('IntersectionObserver' in window)) {
    els.forEach((e) => e.classList.add('in'));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          entry.target.style.animationDelay = `${i * 0.04}s`;
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.08, rootMargin: '0px 0px -8% 0px' }
  );
  els.forEach((e) => io.observe(e));
}
