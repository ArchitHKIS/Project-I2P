import Tkinter as tk
import time


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.running   = False

		self.startTime = 0

		self.timeLabelText = tk.StringVar()
		self.label = tk.Label(textvariable=self.timeLabelText)

		self.label.pack()

		self.runButtonText = tk.StringVar()
		self.runButtonText.set("Run")
		self.runButton = tk.Button(textvariable=self.runButtonText,
								   command=self.__runButton)

		self.runButton.pack()

		self.laps    = []
		self.lapButton = tk.Button(text="Lap",
								   command=self.__lapButton)
		self.lapButton.pack()

		self.bind("<Return>", self.__lapButton)

    def __timelabel(self):

		if self.running:
			seconds = time.time() - self.startTime
			self.timeLabelText.set("%d:%02d:%02d" % seconds_to_time(seconds))
			self.after(1000, self.__timelabel)

    def __runButton(self):

		if self.running:
			self.running = False
			self.runButtonText.set("Run")

		else:

			self.startTime = time.time()

			self.running = True

			self.after(0, self.__timelabel)

			self.runButtonText.set("Stop")

			for lap in self.laps:
				lap.pack_forget()

			self.laps = []

    def __lapButton(self, *args):

		if self.running:

			t = self.timeLabelText.get()
			t = time_to_seconds(t)

			if self.laps:

				elapsed = sum([time_to_seconds(self.laps[x].cget("text").split()[1]) for x in range(len(self.laps))])

				t       = t - elapsed
			t = seconds_to_time(t)
			t = ":".join([str(x) for x in t])
			t = "{0}. {1}".format(len(self.laps)+ 1, t)

			self.laps.append(tk.Label(text=t))

			for lap in self.laps:
				lap.pack()


def time_to_seconds(time):

	h, m, s = [int(x) for x in time.split(':')]
	return h*3600 + m*60 + s

def seconds_to_time(seconds):

	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)
	return h, m, s

if __name__ == '__main__':

	App().mainloop()