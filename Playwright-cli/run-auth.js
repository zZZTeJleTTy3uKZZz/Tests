import { spawn } from 'child_process';
import path from 'path';

console.log('Spawning standalone auth process...');
const env = { ...process.env, DEBUG: 'pw:api,notebooklm:*' };

const child = spawn('npx', ['-y', '@roomi-fields/notebooklm-mcp@latest', 'run', 'setup-auth'], {
  stdio: 'inherit',
  shell: true,
  env
});

child.on('exit', (code) => {
  console.log(`Standalone auth process exited with code ${code}`);
});
