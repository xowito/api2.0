import client from '../db.ts'

export async function find_by_id(id: number | string): Promise<boolean> {
   const result = await client.query('SELECT COUNT(*) count FROM instrumento Where id_instrumento = ?', [id])
   return result[0].count >=1;
}

export async function find_by_almacen(id: number | string): Promise<boolean> {
   const result = await client.query('SELECT COUNT(*) count FROM instrumento Where id_almacen = ?', [id])
   return result[0].count >=1;
}