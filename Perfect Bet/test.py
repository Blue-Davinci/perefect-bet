import time
import progressbar


widgets = [
    ' ', progressbar.Percentage(),
    ' ', progressbar.SimpleProgress(format='(%(value_s)s of %(max_value_s)s)'),
    ' ', progressbar.Bar('>', fill='.'),
    ' ', progressbar.ETA(format_finished='- %(seconds)s  -', format='ETA: %(seconds)s', ),
    ' - ', progressbar.DynamicMessage('loss'),
    ' - ', progressbar.DynamicMessage('error'),
    '                          '
]

bar = progressbar.ProgressBar(redirect_stdout=True, widgets=widgets)
bar.start(100)
for i in range(100):
    time.sleep(0.1)
    bar.update(i + 1, loss=i / 100., error=i)
bar.finish()