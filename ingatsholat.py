#!/usr/bin/env python

from praytimes import PrayTimes
from gi.repository import Notify
from datetime import date
import time

praytime = PrayTimes()

# tune and adjustment based on shalat.landak.com
praytime.adjust({
  'fajr': 20,
  'dhuhr': '2 min',
  'maghrib': 1,
  'isha': 18
})

praytime.tune({
  'fajr': 2,
  'sunrise': -2,
  'asr': 2,
  'maghrib': 2,
  'isha': 2
})

translasi = {
    'imsak': 'Imsak',
    'fajr': 'Subuh',
    'dhuhr': 'Duhur',
    'asr': 'Ashar',
    'maghrib': 'Maghrib',
    'isha': 'Isya\'',
    'sunrise': 'matari terbit',
    'sunset': 'terdengar burung hantu'
}

Notify.init("Ingat Sholat")
notifier = Notify.Notification.new('Sholat dulu..')
waktu_shalat = praytime.getTimes(date.today(), [-6.1744444,106.8294444], 7)

while True:
  jam_sekarang = time.strftime('%H:%M', time.localtime())
  for waktu, jam in waktu_shalat.iteritems():
    if jam==jam_sekarang:
      if waktu in ['asr', 'dhuhr', 'fajr', 'isha', 'maghrib']:
        summary = 'Waktunya sholat {}'.format(translasi[waktu])
        body    = 'segerakan sholat '
      else:
        summary = 'Sekedar info'
        body    = 'Sekarang waktunya {}, rehat sekejap jika kau lelah'.format(translasi[waktu])
      notifier.update(summary, body)
      notifier.show()
  time.sleep(60)
