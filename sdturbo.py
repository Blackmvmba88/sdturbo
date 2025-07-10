import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

fs = 44100
duration = 0.05  # segundos por bloque
blocksize = int(fs * duration)

colors = ['red', 'green', 'blue', 'magenta', 'orange', 'cyan', 'yellow']
color_idx = 0
AMPLIFICATION_FACTOR = 5  # Factor de amplificación para señales bajas
LOW_SIGNAL_THRESHOLD = 0.1  # Umbral para detectar señal baja

plt.ion()
fig, ax = plt.subplots()
fig.set_facecolor('black')  # Fondo negro para la figura
ax.set_facecolor('black')  # Fondo negro para el área de los ejes

x = np.arange(blocksize) / fs
line, = ax.plot(x, np.zeros(blocksize), color=colors[color_idx], linewidth=2, alpha=1.0)
glow_lines = [
    ax.plot(x, np.zeros(blocksize), color=colors[color_idx], linewidth=4, alpha=0.3)[0],
    ax.plot(x, np.zeros(blocksize), color=colors[color_idx], linewidth=6, alpha=0.1)[0]
]

ax.set_ylim(-1, 1)
ax.set_xlim(0, duration)
ax.set_xlabel("Tiempo [s]")
ax.set_ylabel("Amplitud")
ax.set_title("Señal del micrófono en tiempo real", color='white')

# Cambiar color de textos y ticks a blanco
ax.tick_params(colors='white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

try:
    with sd.InputStream(channels=1, samplerate=fs, blocksize=blocksize) as stream:
        print("Presiona Ctrl+C para detener")
        while True:
            audio_block, _ = stream.read(blocksize)
            signal_max = np.max(np.abs(audio_block[:, 0]))

            # Amplificar señal si es muy baja
            if signal_max < LOW_SIGNAL_THRESHOLD:
                audio_block[:, 0] *= AMPLIFICATION_FACTOR

            # Actualizar la línea principal
            line.set_ydata(audio_block[:, 0])
            color_idx = (color_idx + 1) % len(colors)
            line.set_color(colors[color_idx])

            # Actualizar líneas de "glow"
            for i, glow_line in enumerate(glow_lines):
                glow_line.set_ydata(audio_block[:, 0])
                glow_line.set_color(colors[color_idx])

            fig.canvas.draw()
            fig.canvas.flush_events()
except KeyboardInterrupt:
    print("Detenido por el usuario")
except Exception as e:
    print(f"Error: {e}")

# SDTurbo

SDTurbo es una herramienta de visualización en tiempo real de señales de audio capturadas desde el micrófono. Incluye efectos visuales como amplificación automática para señales bajas y un efecto de "glow" dinámico.

## Características

- Visualización en tiempo real de señales de audio.
- Amplificación automática para señales de baja amplitud.
- Efecto de "glow" dinámico para mejorar la estética.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/sdturbo.git
   cd sdturbo
   ```

### **3. Crear el archivo [requirements.txt](http://_vscodecontentref_/1)**
Incluye las dependencias necesarias para el proyecto:

```plaintext
numpy
sounddevice
matplotlib
```
