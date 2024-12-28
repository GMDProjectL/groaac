pkgname=groaac
pkgver=1.0
pkgrel=1
pkgdesc="Extract MP3s from MP4 files"
arch=('any')
url="https://github.com/GMDProjectL/groaac"
license=('GPL')
depends=('python-wxpython' 'ffmpeg' 'python-dbus')
makedepends=()
checkdepends=()
optdepends=()
backup=()
options=()
install=
source=("config_utils.py" "ffmpeg_utils.py" "main.py" "groaac.png" "groaac.desktop")

package() {
  mkdir -p "$pkgdir/opt/groaac"
  install -Dm7777 "$srcdir/config_utils.py" "$pkgdir/opt/groaac"
  install -Dm7777 "$srcdir/ffmpeg_utils.py" "$pkgdir/opt/groaac"
  install -Dm7777 "$srcdir/main.py" "$pkgdir/opt/groaac"
  install -Dm7777 "$srcdir/groaac.png" "$pkgdir/opt/groaac"
  install -Dm0644 $srcdir/groaac.desktop -t "${pkgdir}/usr/share/applications"
}