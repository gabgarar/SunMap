from Implements.Event import Event
from sunpy.net import Fido, attrs as a
import astropy.units as u


class DownloadEvent(Event):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getDescription(self):
        return " Download : Download a FITS image from a date"

    def execute(self, mmap, comm):

        if not comm or len(comm) < 5:
            print(self.getDescription())
        else:
            soon = str(comm.pop(0));
            late = str(comm.pop(0));
            inst = str(comm.pop(0));
            wave = int(comm.pop(0));
            dif = int(comm.pop(0));

            if wave == 0:
                searchs = Fido.search(a.Time(soon, late), a.Instrument(inst),
                                  a.vso.Sample(dif * u.minute))
            else:
                searchs = Fido.search(a.Time(soon, late), a.Instrument(inst), a.Wavelength(wave * u.angstrom),
                                      a.vso.Sample(dif * u.minute))

            print(searchs)
            Fido.fetch(searchs, path='{instrument}/{file}')

            ''' How to use :
                soon = '2012/3/4'
                late = '2012/3/5'
                wave = 171
                inst = 'aia'
                dif = 60
            '''
