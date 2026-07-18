// Ported from echo/frontend/helperJS/theme.js — same read-CSS-vars-live
// pattern, same withAlpha hex parser. Renamed getThemeColors -> readTokens
// only because this project's token names differ from Echo's (--ink vs
// --text); the mechanism is unchanged.

export function readTokens(el = document.documentElement) {
  const styles = getComputedStyle(el);
  return {
    ink: styles.getPropertyValue('--ink').trim(),
    muted: styles.getPropertyValue('--muted').trim(),
    accent: styles.getPropertyValue('--accent').trim(),
    line: styles.getPropertyValue('--line').trim(),
    panel: styles.getPropertyValue('--panel').trim(),
  };
}

export function withAlpha(color, alpha) {
  const hex = color.replace('#', '');
  let r, g, b;
  if (hex.length === 3) {
    r = parseInt(hex.charAt(0) + hex.charAt(0), 16);
    g = parseInt(hex.charAt(1) + hex.charAt(1), 16);
    b = parseInt(hex.charAt(2) + hex.charAt(2), 16);
  } else if (hex.length >= 6) {
    r = parseInt(hex.slice(0, 2), 16);
    g = parseInt(hex.slice(2, 4), 16);
    b = parseInt(hex.slice(4, 6), 16);
  } else {
    // token already an rgba()/color-mix() string (e.g. dark-mode --panel) — pass through
    return color;
  }
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}
