---
title: "Guía de instalación: Python + VS Code + Git + GitHub"
subtitle: "Tópicos de Finanzas Avanzadas · Semana 0"
author: "Econ. Jonathan Rosas, MSc."
date: "Semestre 2026"
lang: es
---

# Antes de empezar

Esta guía te deja el entorno completo del curso instalado en tu PC en unos 30–40 minutos. Solo se hace **una vez**. Al terminar podrás abrir los notebooks del curso en Visual Studio Code, ejecutarlos y entregar tus prácticas mediante GitHub.

Necesitas: una PC con Windows 10/11 (al final hay notas para Mac), conexión a internet y un correo electrónico al que tengas acceso.

Si tu PC es muy limitada o algo falla, el plan B siempre es **Google Colab** (colab.research.google.com): abre los notebooks desde el navegador sin instalar nada. Pero la meta del curso es que domines el entorno profesional: VS Code + Git.

---

# Paso 1: Instalar Python

1. Entra a **https://www.python.org/downloads/** y descarga la última versión estable de Python 3 (3.12 o superior).
2. Ejecuta el instalador. **MUY IMPORTANTE:** en la primera pantalla marca la casilla **"Add python.exe to PATH"** antes de hacer clic en *Install Now*. Si olvidas esto, VS Code no encontrará Python.
3. Verifica la instalación: abre el menú Inicio, escribe `cmd`, abre el *Símbolo del sistema* y escribe:

```
python --version
```

Debe responder algo como `Python 3.12.x`. Si dice que no se reconoce el comando, desinstala Python y repite el paso 2 marcando la casilla del PATH.

> **Nota:** en este curso NO usamos Anaconda. Si ya la tienes instalada no hace falta desinstalarla, pero el entorno del curso lo crearemos con `venv`, el mecanismo estándar de Python.

# Paso 2: Instalar Visual Studio Code

1. Descarga VS Code desde **https://code.visualstudio.com** e instálalo (acepta las opciones por defecto; recomiendo dejar marcada la opción "Agregar la acción 'Abrir con Code' al menú contextual").
2. Abre VS Code. En la barra lateral izquierda, haz clic en el icono de **Extensiones** (cuatro cuadritos) e instala:
   - **Python** (de Microsoft),
   - **Jupyter** (de Microsoft),
   - *(opcional)* **Spanish Language Pack** si prefieres el editor en español.

# Paso 3: Instalar Git

Git es el sistema de control de versiones con el que entregarás tus prácticas.

1. Descarga Git desde **https://git-scm.com/downloads** y ejecuta el instalador.
2. El instalador hace muchas preguntas: **acepta todas las opciones por defecto** (siguiente, siguiente…). Eso instala también el *Git Credential Manager*, que luego conecta tu PC con GitHub sin contraseñas.
3. Cierra y vuelve a abrir VS Code (para que detecte Git). Verifica en una terminal:

```
git --version
```

4. Configura tu identidad: es la "firma" que llevará cada entrega tuya. Usa **el mismo correo** con el que crearás tu cuenta de GitHub:

```
git config --global user.name  "Nombre Apellido"
git config --global user.email "tucorreo@ejemplo.com"
```

# Paso 4: Crear tu cuenta de GitHub y conectarla a VS Code

1. Entra a **https://github.com**  *Sign up*. Consejos:
   - Elige un **nombre de usuario profesional** (p. ej. `jperez-econ`, no `gamer_killer99`): aparecerá en tu CV y en tu portafolio.
   - Regístrate con un correo personal que no pierdas al egresar; puedes añadir el institucional después (te da acceso al *GitHub Student Developer Pack*, gratis).
2. Verifica tu correo (GitHub te envía un código).
3. Conecta VS Code con GitHub: en VS Code haz clic en el icono de **Cuentas** (una silueta, abajo a la izquierda)  **Sign in with GitHub**  se abre el navegador  *Authorize Visual Studio Code*. Listo: tu PC ya puede subir y bajar código de tu cuenta sin pedirte claves cada vez.

# Paso 5: Fork y clonación del repositorio del curso

El material del curso vive en un repositorio público. Tú trabajarás sobre **tu propia copia** (un *fork*).

1. **Fork (una sola vez):** entra al repositorio del curso (el enlace está en el aula virtual), haz clic en el botón **Fork** (arriba a la derecha)  *Create fork*. Ahora existe `github.com/TU-USUARIO/topicos-finanzas-upao`.
2. **Clonar tu fork (una sola vez):**
   - En tu fork, botón verde **Code**  pestaña HTTPS  copia la URL.
   - En VS Code: `Ctrl+Shift+P`  escribe **Git: Clone**  pega la URL  elige una carpeta (p. ej. `Documentos\finanzas-avanzadas`)  *Open* cuando pregunte.
3. Ya tienes el curso en tu PC. En el explorador de VS Code verás las carpetas `01_fundamentos_valor`, `utils`, etc.

# Paso 6: Crear el entorno del curso e instalar las librerías

En VS Code, abre una terminal (`Ctrl+ñ` o menú *Terminal  New Terminal*) y ejecuta, una línea a la vez:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

- La primera línea crea un **entorno virtual** propio del curso (carpeta `.venv`): así las librerías del curso no chocan con nada más de tu PC.
- Si la activación da un error de "ejecución de scripts deshabilitada", abre PowerShell como administrador y ejecuta `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`, luego reintenta.
- La tercera instala todas las librerías del curso (pandas, statsmodels, yfinance, arch, scikit-learn, etc.). Tarda unos minutos.

Por último, abre `01_fundamentos_valor/clase01_practica.ipynb`. Arriba a la derecha del notebook haz clic en **Select Kernel**  *Python Environments*  elige **.venv**. Ejecuta la primera celda con `Shift+Enter`. Si corre sin errores: tu entorno está listo.

# Paso 7: El flujo de cada semana

**Antes de clase (traer el material nuevo):**

1. En la página de tu fork en GitHub: botón **Sync fork**  *Update branch* (copia lo nuevo del repo del docente a tu fork).
2. En VS Code: panel **Source Control** (icono de ramas)  menú `…`  **Pull** (baja lo nuevo a tu PC).

**Después de trabajar (entregar):**

1. Guarda tus cambios en el notebook.
2. Panel **Source Control**  verás tus archivos modificados  escribe un mensaje claro (p. ej. `semana 1: modelo insignia + interpretaciones`)  botón **Commit**  botón **Sync Changes** (esto hace el *push* a GitHub).
3. Entra a tu fork en el navegador y verifica que tu notebook aparezca actualizado. **La fecha y hora del commit es tu constancia de entrega.**

# Problemas frecuentes

| Síntoma | Solución |
|---|---|
| `python` no se reconoce en la terminal | Reinstalar Python marcando *Add python.exe to PATH*; cerrar y reabrir VS Code. |
| VS Code no ofrece `.venv` como kernel | Verifica que creaste el venv dentro de la carpeta del curso; `Ctrl+Shift+P`  *Python: Select Interpreter*  `.venv`. |
| Error al activar el venv en PowerShell | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` y reintentar. |
| `pip install` falla por SSL o red | Prueba desde otra red (el wifi de algunas instituciones bloquea PyPI) o usa datos móviles solo para la instalación. |
| VS Code pide credenciales al hacer push | Icono de Cuentas  *Sign in with GitHub*; o actualiza Git a la última versión (incluye Git Credential Manager). |
| Hiciste cambios en el repo equivocado | Trabaja siempre dentro de la carpeta clonada de **tu fork**; el repo del docente es de solo lectura para ti. |
| Nada funciona y la clase ya empezó | Abre el notebook de la semana en **Google Colab** y resuelve la instalación después de clase. |

# Notas para Mac

- Python: instala desde python.org igual que en Windows (o con Homebrew: `brew install python`).
- Git: al escribir `git --version` en la Terminal, macOS ofrece instalar las *Command Line Tools*; acepta.
- La activación del venv cambia a: `source .venv/bin/activate`.
- Todo lo demás (VS Code, extensiones, GitHub, flujo semanal) es idéntico.

---

**Checklist final**, marca antes de la clase 2:

- [ ] `python --version` responde 3.12+
- [ ] VS Code con extensiones Python y Jupyter
- [ ] `git --version` responde y configuraste `user.name` / `user.email`
- [ ] Cuenta de GitHub creada y conectada a VS Code
- [ ] Fork del repo del curso creado y clonado en tu PC
- [ ] `.venv` creado, `requirements.txt` instalado y el notebook de la semana 1 corre
- [ ] Primer commit + push hecho (aparece en tu fork en github.com)
