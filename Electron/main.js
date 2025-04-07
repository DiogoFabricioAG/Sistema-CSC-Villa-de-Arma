const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let flaskProcess;

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
    },
  });

  win.loadURL('http://localhost:5173');
}

function startFlask() {
  const isWin = process.platform === "win32";
  const cmd = isWin ? "python" : "python3";

  flaskProcess = spawn(cmd, ["../Backend/app.py"], {
    cwd: __dirname,
    env: process.env,
    shell: true,
  });

  flaskProcess.stdout.on('data', (data) => {
    console.log(`[Flask] ${data}`);
  });

  flaskProcess.stderr.on('data', (data) => {
    console.error(`[Flask Error] ${data}`);
  });

  flaskProcess.on('close', (code) => {
    console.log(`Flask server closed with code ${code}`);
  });
}

app.whenReady().then(() => {
  startFlask();
  createWindow();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function () {
  if (flaskProcess) flaskProcess.kill();
  if (process.platform !== 'darwin') app.quit();
});
