// Track intent only. This module never treats opening WhatsApp as a confirmed lead.
// Meta Pixel / GA4 base tags must be configured separately before remote events exist.
type TrackingWindow = Window & { fbq?: (...args: unknown[]) => void; gtag?: (...args: unknown[]) => void };
const trackingWindow = window as TrackingWindow;
const attributionKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'] as const;
const query = new URLSearchParams(window.location.search);
const campaign: Record<string, string> = {};
for (const key of attributionKeys) {
  const value = query.get(key);
  // Campaign labels only; no freeform form input, full URL, fbclid, or personal details.
  if (value && /^[a-zA-Z0-9_.~-]{1,100}$/.test(value)) campaign[key] = value;
}
export function trackWhatsAppClick(location: string) {
  const detail = { cta_location: location, page_path: window.location.pathname, ...campaign };
  window.dispatchEvent(new CustomEvent('khuncode:whatsapp-click', { detail }));
  try { trackingWindow.fbq?.('trackCustom', 'WhatsAppClick', detail); } catch { /* Navigation must still work. */ }
  try { trackingWindow.gtag?.('event', 'click_whatsapp', detail); } catch { /* Navigation must still work. */ }
}
// Keep campaign labels when a visitor moves to another internal marketing page.
if (Object.keys(campaign).length) {
  document.querySelectorAll<HTMLAnchorElement>('a[href]').forEach(anchor => {
    const url = new URL(anchor.href, window.location.href);
    if (url.origin !== window.location.origin || anchor.getAttribute('href')?.startsWith('#')) return;
    for (const [key, value] of Object.entries(campaign)) if (!url.searchParams.has(key)) url.searchParams.set(key, value);
    anchor.href = url.href;
  });
}
document.addEventListener('click', event => {
  const anchor = event.target instanceof Element ? event.target.closest<HTMLAnchorElement>('a[data-track-cta="whatsapp"]') : null;
  if (anchor) trackWhatsAppClick(anchor.dataset.location || 'unknown');
});
