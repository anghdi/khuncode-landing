import { readFileSync } from 'node:fs';
import { strict as assert } from 'node:assert';
import vm from 'node:vm';
import { transformSync } from 'esbuild';
const source = readFileSync(new URL('../src/scripts/lead-tracking.ts', import.meta.url), 'utf8');
const code = transformSync(source, { loader: 'ts', format: 'cjs' }).code;
function run(search, fail = false) {
  const events = [], remote = [], listeners = {};
  class Element {}
  const links = ['/kontak', '#hasil-kerja', 'https://wa.me/6285117304509'].map(raw => ({ href: new URL(raw, 'https://khuncode.com/ecommerce').href, getAttribute: () => raw }));
  const context = { exports: {}, module: { exports: {} }, URL, URLSearchParams, Element,
    CustomEvent: class { constructor(type, options) { this.type = type; this.detail = options.detail; } },
    window: { location: { search, pathname: '/ecommerce', href: 'https://khuncode.com/ecommerce'+search, origin: 'https://khuncode.com' }, dispatchEvent: e => events.push(e), fbq: (...args) => { if (fail) throw Error('blocked'); remote.push(args); }, gtag: (...args) => remote.push(args) },
    document: { querySelectorAll: () => links, addEventListener: (name, fn) => { listeners[name] = fn; } }
  };
  vm.runInNewContext(code, context);
  const target = new Element(); target.closest = () => ({ href: 'https://wa.me/6285117304509', dataset: { trackCta: 'whatsapp', location: 'ecommerce-hero' } });
  listeners.click({ target });
  return { events, remote, links, context };
}
const tracked = run('?utm_source=instagram&utm_campaign=launch_01&fbclid=private&email=private');
assert.equal(tracked.events.length, 1);
assert.equal(tracked.remote.length, 2);
assert.equal(tracked.remote[0][1], 'WhatsAppClick');
assert.equal(tracked.remote[1][1], 'click_whatsapp');
assert.equal(tracked.events[0].detail.utm_source, 'instagram');
assert.equal(tracked.events[0].detail.fbclid, undefined);
assert.equal(tracked.events[0].detail.email, undefined);
assert.ok(tracked.links[0].href.includes('utm_source=instagram'));
assert.ok(!tracked.links[1].href.includes('utm_source'));
assert.ok(!tracked.links[2].href.includes('utm_source'));
assert.equal(run('?utm_source=name%40email.com').events[0].detail.utm_source, undefined);
assert.equal(run('', true).events.length, 1);
const disabled = run('');
delete disabled.context.window.fbq; delete disabled.context.window.gtag;
assert.doesNotThrow(() => disabled.context.module.exports.trackWhatsAppClick('contact-inquiry'));
assert.equal(disabled.events.length, 2);
assert.ok(!JSON.stringify(tracked.remote).includes('"Lead"'));
console.log('PASS: click semantics, UTM allowlist, internal propagation, no PII fields, missing/blocked trackers.');
