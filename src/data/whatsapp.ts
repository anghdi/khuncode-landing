export const WHATSAPP_NUMBER = '6285117304509';

export const defaultInquiryMessage = `Halo KhunCode, saya tertarik membuat website toko online.

Nama bisnis:
Produk yang dijual:
Jumlah produk:
Sistem pesanan: WhatsApp / checkout
Target website selesai:

Saya ingin konsultasi paket yang cocok.`;

export const createWhatsAppUrl = (message = defaultInquiryMessage) =>
  `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;

export const createPackageInquiryMessage = (name: string, price: string, starting = false) =>
  `Halo KhunCode, saya tertarik dengan paket ${name} ${starting ? 'mulai ' : ''}Rp${price}.

Nama bisnis:
Produk yang dijual:
Jumlah produk:
Sistem pesanan: WhatsApp / checkout
Target website selesai:

Saya ingin konsultasi paket yang cocok.`;
