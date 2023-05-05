<h1>Telegram Bot ile RSS Beslemesi Takibi</h1>

<p>Telegram botunuzun web sitenizde paylaşılan gönderileri 1 dakika ara ile kontrol ederek Telegram kanalınızda paylaşabilen bir sistemdir.</p>

<h3 align="center">Telegram Bot ile RSS Beslemesi Takibi</h3>
<p align="center">
  <strong>Python betiği, bir RSS beslemesini takip eder ve yeni gönderileri Telegram kanalınıza gönderir</strong>
  <br>
  <br>
  <a href="#nasıl-kullanılır">Nasıl Kullanılır</a>
  ·
  <a href="#özellikler">Özellikler</a>
  ·
  <a href="#lisans">Lisans</a>
</p>
<br>
<h2>Nasıl Kullanılır?</h2>
Gerekli kütüphaneleri yükleyin:
<code>pip install feedparser</code>
<code>pip install telegram</code>
<code>pip install asyncio</code>
RSS beslemesi URL'sini rss_url değişkenine girin.

Telegram botunuzun bot tokenını ve chat_id'sini belirleyin.

Betiği çalıştırın!

<h2>Özellikler</h2>
RSS beslemesi sürekli olarak takip edilir ve yeni gönderiler keşfedilir.
Yeni gönderiler, Telegram kanalınıza gönderilir.
Daha önceden görülmüş gönderiler, bir set içinde takip edilir ve aynı gönderi birden fazla kez gönderilmez.

<h2>Lisans</h2>
Bu betik, MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
