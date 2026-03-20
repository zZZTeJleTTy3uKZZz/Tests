import { spawn } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

console.log('Starting auth setup...');
const child = spawn('npx', ['-y', '@roomi-fields/notebooklm-mcp@latest', 'setup-auth'], {
  stdio: 'inherit',
  shell: true
});

child.on('exit', (code) => {
  console.log(`Process exited with code ${code}`);
});
