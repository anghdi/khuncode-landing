from pathlib import Path
import json,re
root=Path('C:/laragon/www/khuncode-landing')
plans=[
 dict(id='starter',name='Starter',price='1.500.000',starting=False,description='Langkah pertama agar bisnis kamu mudah ditemukan dan dihubungi.',audience='Untuk usaha kecil, personal brand, jasa, atau bisnis yang baru membutuhkan website.',pages='Maksimal 3 halaman',revision='1x revisi',features=['Maksimal 3 halaman','Desain responsif mobile & desktop','Desain menyesuaikan identitas bisnis','Tombol WhatsApp','Informasi layanan / produk','Kontak & social media','Form kontak sederhana','Google Maps jika dibutuhkan','Basic SEO','Optimasi gambar','SSL / HTTPS','Deploy website','1x revisi']),
 dict(id='business',name='Business',price='2.500.000',starting=False,description='Ruang lebih lengkap untuk memperkenalkan bisnis dan membangun kepercayaan.',audience='Untuk company profile dan bisnis yang membutuhkan website lebih lengkap.',pages='Maksimal 7 halaman',revision='2x revisi',features=['Maksimal 7 halaman','Semua fitur Starter','Desain lebih custom','Halaman layanan lebih lengkap','Portfolio / galeri','Testimoni','FAQ','Form inquiry','CTA WhatsApp di beberapa bagian','Basic SEO tiap halaman','Sitemap','Setup Google Search Console','Optimasi dasar performa website','Social preview saat link dibagikan','2x revisi']),
 dict(id='custom',name='Custom',price='4.000.000',starting=True,description='Website yang bekerja mengikuti alur dan kebutuhan khusus bisnismu.',audience='Untuk website dengan fungsi khusus, termasuk booking dan e-commerce.',pages='Halaman sesuai kebutuhan',revision='Revisi sesuai scope',features=['Jumlah halaman menyesuaikan kebutuhan','Desain custom','Semua kebutuhan dasar dari Business','Booking jadwal','Pemesanan layanan','Katalog produk','Filter / pencarian','Form custom','Login user','Dashboard sederhana','Database','Payment gateway','Integrasi API','Email / WhatsApp notification','Fitur khusus sesuai kebutuhan project','Revisi menyesuaikan scope'])]
(root/'src/data').mkdir(exist_ok=True)
(root/'src/data/packages.ts').write_text('export const packages = '+json.dumps(plans,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
(root/'src/components/PackagePricing.astro').write_text('''---
import { packages } from '../data/packages';
interface Props { detailed?: boolean; }
const { detailed = false } = Astro.props;
---
<div class="package-grid">{packages.map((plan,i) => <article id={detailed ? plan.id : undefined} class:list={['package-card',{'package-business': i === 1}]}>
  <p class="package-kicker">{i === 0 ? 'MULAI HADIR ONLINE' : i === 1 ? 'KENALKAN BISNIS LEBIH LENGKAP' : 'UNTUK KEBUTUHAN KHUSUS'}</p>
  <h2 class="package-name">{plan.name}</h2><p class="package-copy">{detailed ? plan.audience : plan.description}</p>
  <div class="package-amount"><span>{plan.starting ? 'Mulai dari' : 'Biaya pembuatan'}</span><strong>Rp{plan.price}</strong></div>
  <ul class="package-summary"><li>{plan.pages}</li><li>{plan.revision}</li><li>{i === 0 ? 'Responsive, WhatsApp & basic SEO' : i === 1 ? 'Semua fitur Starter + fitur bisnis' : 'Fitur dipilih sesuai scope project'}</li></ul>
  {detailed ? <details class="package-features"><summary>Lihat semua fitur <span aria-hidden="true">+</span></summary>{plan.starting && <p class="package-scope">Pilihan fitur di bawah disesuaikan dengan kebutuhan. Harga final mengikuti scope dan integrasi yang disepakati.</p>}<ul>{plan.features.map(feature => <li>{feature}</li>)}</ul></details> : <a class="package-detail-link" href={`/harga#${plan.id}`}>Lihat semua fitur ↗</a>}
  <a class="button package-button" href={`https://wa.me/6285117304509?text=${encodeURIComponent(`Halo KhunCode, saya tertarik paket ${plan.name} ${plan.starting ? 'mulai ' : ''}Rp${plan.price}, dengan deploy + maintenance Rp100.000/bulan dan domain terpisah. Saya ingin mendiskusikan kebutuhan website.`)}`} target="_blank" rel="noopener noreferrer">{plan.starting ? 'Diskusikan kebutuhan' : `Pilih ${plan.name}`} <span aria-hidden="true">↗</span></a>
</article>)}</div>
<aside class="package-costs" aria-label="Biaya untuk semua paket"><p><strong>Deploy + maintenance</strong><span>Rp100.000/bulan untuk semua paket.</span></p><p><strong>Domain terpisah</strong><span>Sesuai harga domain yang dipilih client.</span></p></aside>
''',encoding='utf-8')
p=root/'src/pages/harga.astro'
p.write_text('''---
import Layout from '../layouts/Layout.astro';
import PackagePricing from '../components/PackagePricing.astro';
---
<Layout title="Paket Website Starter, Business & Custom | KhunCode" description="Starter Rp1.500.000, Business Rp2.500.000, Custom mulai Rp4.000.000. Deploy + maintenance Rp100.000/bulan. Domain terpisah.">
<section class="section wrap inner-page packages-page"><header class="page-heading packages-heading"><p class="eyebrow">PAKET WEBSITE KHUNCODE</p><h1>Mulai dari kebutuhan.<br /><em>Pilih yang pas untuk bisnismu.</em></h1><p>Dari website pertama sampai sistem dengan fungsi khusus. Pilih cakupan yang sesuai, lalu kita bangun bersama.</p></header>
<PackagePricing detailed />
<p class="package-footnote">Starter dan Business mengikuti batas halaman serta revisi paket. Untuk Custom, jumlah halaman, fitur, integrasi, dan revisi ditentukan dalam scope project. Layanan pihak ketiga yang diperlukan dibahas sebelum pengerjaan.</p>
<aside class="next-step"><div><h2>Belum yakin paket mana?</h2><p>Ceritakan kebutuhan bisnismu. Kami bantu menentukan cakupan yang tepat.</p></div><a class="text-link" href="/kontak">Diskusi dulu ↗</a></aside></section>
</Layout>
''',encoding='utf-8')
p=root/'src/pages/index.astro';s=p.read_text(encoding='utf-8-sig')
s=s.replace("import Layout from '../layouts/Layout.astro';","import Layout from '../layouts/Layout.astro';\nimport PackagePricing from '../components/PackagePricing.astro';")
s=re.sub(r'const plans = \[.*?\n\];\n','',s,flags=re.S)
a=s.index('    <div class="compact-plan-grid">');b=s.index('    <div class="compact-studio">',a)
s=s[:a]+'    <PackagePricing />\n'+s[b:]
s=s.replace('LAYANAN & HARGA AWAL','PAKET WEBSITE').replace('Apa yang ingin kamu bangun?','Pilih yang pas untuk bisnismu.')
p.write_text(s,encoding='utf-8')
p=root/'src/pages/ecommerce.astro';s=p.read_text(encoding='utf-8-sig').replace('Rp2.500.000','Rp4.000.000').replace('Rp2,5 juta','Rp4 juta')
s=s.replace('Biaya development. Domain & hosting terpisah.','Paket Custom. Deploy + maintenance Rp100.000/bulan. Domain terpisah.')
s=s.replace('Yang termasuk dalam website kamu.','Fitur sesuai kebutuhan toko kamu.')
s=s.replace('Payment gateway, ongkir otomatis, dan kebutuhan khusus dibahas terpisah.','Katalog, checkout, payment gateway, dan integrasi dipilih sesuai scope. Harga final disepakati sebelum pengerjaan.')
s=s.replace('Website e-commerce mulai Rp4.000.000.<br />','Custom mulai Rp4.000.000 + deploy & maintenance Rp100.000/bulan. Domain terpisah.<br />')
p.write_text(s,encoding='utf-8')
css='''
/* Unified three-tier pricing: restrained surfaces, clear costs, native disclosures. */
.package-grid { display: grid; grid-template-columns: repeat(3,minmax(0,1fr)); gap: 20px; align-items: start; }
.package-card { min-width: 0; padding: 28px; border: 1px solid var(--line); border-radius: 20px; background: #fff; scroll-margin-top: 30px; }
.package-business { background: #f4f7ff; border-color: #a9bfff; }
.package-kicker { color: var(--muted); font-size: 9px; letter-spacing: .08em; min-height: 29px; }
.section .package-name { font-size: 27px; font-weight: 600; margin-top: 8px; letter-spacing: -.04em; }
.package-copy { font-size: 14px; line-height: 1.75; color: var(--muted); margin-top: 14px; min-height: 74px; }
.package-amount { padding-block: 24px; border-bottom: 1px solid var(--line); }
.package-amount>span { display: block; font-size: 11px; color: var(--muted); margin-bottom: 8px; }
.package-amount strong { font-size: clamp(25px,2.5vw,34px); font-weight: 600; letter-spacing: -.05em; white-space: nowrap; }
.package-summary { padding-block: 22px; display: grid; gap: 9px; }
.package-summary li { font-size: 13px; line-height: 1.7; padding-left: 16px; position: relative; }
.package-summary li::before { content: '✓'; position: absolute; left: 0; color: var(--accent); font-size: 11px; }
.package-detail-link { display: inline-flex; align-items: center; min-height: 44px; font-size: 13px; text-decoration: underline; text-underline-offset: 4px; }
.package-button { width: 100%; font-size: 13px; margin-top: 14px; border-radius: 999px; }
.package-features summary { display: flex; justify-content: space-between; cursor: pointer; list-style: none; font-size: 13px; min-height: 44px; align-items: center; border-top: 1px solid var(--line); }
.package-features summary::-webkit-details-marker { display: none; }
.package-features[open] summary span { transform: rotate(45deg); }
.package-features ul { display: grid; gap: 10px; padding: 16px 0; }
.package-features li { font-size: 13px; line-height: 1.7; padding-left: 14px; position: relative; }
.package-features li::before { content: '–'; position: absolute; left: 0; }
.package-scope,.package-footnote { font-size: 12px; line-height: 1.85; color: var(--muted); margin-top: 12px; }
.package-costs { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; padding: 24px 0; margin-top: 22px; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
.package-costs p { font-size: 13px; line-height: 1.85; }.package-costs strong,.package-costs span { display: block; }.package-costs span { color: var(--muted); }
.packages-heading { text-align: center; max-width: 850px; margin-inline: auto; }.packages-heading>p:last-child { margin-inline: auto; }
.packages-heading h1 { font-size: clamp(35px,4vw,55px); }
@media(max-width:1099px) { .package-grid { gap: 14px; }.package-card { padding: 20px; }.package-copy { min-height: 100px; }.package-amount strong { font-size: 27px; } }
@media(max-width:767px) { .package-grid { grid-template-columns: 1fr; gap: 16px; }.package-card { padding: 22px; }.package-kicker,.package-copy { min-height: 0; }.package-copy { margin-top: 10px; }.package-amount { padding-block: 18px; }.package-amount strong { font-size: 30px; }.package-summary { padding-block: 16px; }.package-costs { grid-template-columns: 1fr; gap: 16px; }.compact-landing .package-card { display: grid; grid-template-columns: 1fr auto; column-gap: 12px; }.compact-landing .package-copy,.compact-landing .package-summary { display: none; }.compact-landing .package-kicker { grid-column: 1 / -1; }.compact-landing .package-amount { border: 0; padding: 0; grid-column: 2; grid-row: 2 / 4; align-self: center; }.compact-landing .package-amount strong { font-size: 24px; }.compact-landing .package-button { grid-column: 1 / -1; }.compact-landing .package-detail-link { grid-column: 1; } }
'''
p=root/'src/styles/global.css';p.write_text(p.read_text(encoding='utf-8-sig')+css,encoding='utf-8')
p=root/'PRD.md';s=p.read_text(encoding='utf-8-sig')
start=s.index('# HARGA');end=s.index('# PROSES',start)
pricing='# HARGA\n\nSumber data implementasi: `src/data/packages.ts`. Tiga paket berikut menggantikan seluruh penawaran harga sebelumnya.\n\n'
for plan in plans:
 pricing+='### '+plan['name']+' — '+('Mulai ' if plan['starting'] else '')+'Rp'+plan['price']+'\n\n'+plan['audience']+'\n\n'+'\n'.join('* '+f for f in plan['features'])+'\n\n'
pricing+='Untuk Custom, daftar fitur adalah pilihan sesuai scope, bukan seluruh fitur otomatis termasuk harga awal.\n\n**Domain:** terpisah sesuai harga domain yang dipilih client.\n\n**Deploy + maintenance:** Rp100.000/bulan untuk semua paket.\n\nStarter dan Business adalah harga paket; Custom adalah harga awal. Tampilkan biaya bulanan dan domain dekat paket, bukan hanya di footer.\n\n---\n\n'
s=s[:start]+pricing+s[end:]
s=s.replace('Website E-Commerce mulai dari Rp2.500.000','Website E-Commerce (Custom) mulai dari Rp4.000.000').replace('**Mulai dari Rp2.500.000**','**Custom mulai dari Rp4.000.000**').replace('website e-commerce mulai Rp2.500.000','website e-commerce Custom mulai Rp4.000.000')
s+='\n## Revisi paket terbaru\n\nHomepage tetap ringkas: tiga kartu dengan harga, link rincian, dan CTA. Halaman harga memakai disclosure native untuk fitur lengkap. Business menampilkan 2x revisi sebagai pengganti 1x revisi Starter; Custom mengikuti scope. Estetika referensi: whitespace bersih, tipografi jelas, tombol membulat; identitas biru logo tetap dipakai. Meta Pixel dan GA4 tetap ditunda.\n'
p.write_text(s,encoding='utf-8')
print('Updated shared packages, pricing component, homepage, pricing page, ecommerce, CSS, and PRD.')
