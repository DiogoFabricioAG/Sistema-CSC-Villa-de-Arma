✨ **Sistema de Gestión de Socios - CSC Villa de Arma** ⚽️

💻 Aplicación de escritorio para registrar y gestionar asistencias ✅ y deudas 💰 de los socios del Club Social Cultural Villa de Arma. La app se ejecuta **localmente** 🏠 en una sola PC, **sin necesidad de conexión a internet** 🌐❌.

🛠️ **Tecnologías utilizadas** ⚙️
* **Vue 3:** ⚛️ Frontend moderno con Vite.
* **Flask:** 🐍 API backend en Python.
* **SQLite:** 💾 Base de datos local, liviana y sin servidor.
* **Electron:** ⚡ Empaquetado como aplicación de escritorio.


📂 **Estructura del proyecto** 🌳
* `backend/` → ⚙️ Código del backend en Flask.
* `frontend/` → 🎨 Código del frontend en Vue.
* `Electron/` → 📦 Configuración y archivo principal de Electron.

* `README` → 📄 Este archivo.

🚀 **Cómo ejecutar el proyecto** ▶️
1.  **Clonar el repositorio:** `git clone https://github.com/tu-usuario/tu-repo.git` ⬇️
2.  **Instalar dependencias del frontend (Vue):**
    ```bash
    cd frontend
    npm install
    npm run dev
    ```
3.  **Instalar dependencias del backend (Flask):**
    ```bash
    cd ../backend
    pip install flask flask-cors flask-sqlalchemy
    ```
4.  **Instalar dependencias de Electron:**
    ```bash
    cd ..
    npm install
    ```
5.  **Ejecutar la app de escritorio:** `npm start` 🚀

📦 **Modo producción** 🏭
Cuando el desarrollo esté terminado, puedes construir el frontend con:

```bash
cd frontend
npm run build
```

Esto genera los archivos finales en frontend/dist, que Electron puede cargar directamente.

**✨ Funcionalidades 🌟**

- ➕ **Registro de nuevos socios.**
- 🚶 **Registro de asistencias.**
- 💸 **Registro de deudas y pagos.**
- 📊 **Visualización local de la información.**
- 📶❌ **Funcionamiento sin internet.**

**👨‍💻 Autor ✍️**
Desarrollado por **Diogo Abregu.**






