import sql from '$lib/server/db';

export const load = async () => {
    const usuarios = await sql`SELECT id, nombre FROM usuarios`;
    return { usuarios: [...usuarios] };
};