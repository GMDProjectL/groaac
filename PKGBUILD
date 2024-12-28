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
  cp -r "$srcdir/config_utils.py" "$pkgdir/opt/groaac"
  cp -r "$srcdir/ffmpeg_utils.py" "$pkgdir/opt/groaac"
  cp -r "$srcdir/main.py" "$pkgdir/opt/groaac"
  cp -r "$srcdir/groaac.png" "$pkgdir/opt/groaac"
  install -Dm0644 $srcdir/groaac.desktop -t "${pkgdir}/usr/share/applications"
}