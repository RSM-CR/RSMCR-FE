import postgres from 'postgres';
import { env } from '$env/dynamic/private';

if (!env.DATABASE_URL) throw new Error('Falta DATABASE_URL en el .env');

const sql = postgres(env.DATABASE_URL);

export default sql;