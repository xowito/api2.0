import client from '../db.ts';


interface Params{
    id? : string | number
}

export async function search(params: Params = {}){
    const isSpecific =  Object.keys(params).length !== 0;

    if (isSpecific) {
        return await client.execute('SELECT * from instrumento WHERE id_instrumento = ?', [params.id]);
    } else {
        return await client.execute('SELECT * from instrumento');
    }
    

}

interface InsertParams {
    nombre: string,
    stock: number
}
export async function insert({nombre, stock}: InsertParams){
   return await client.execute('INSERT INTO instrumento(nombre, stock) VALUES (?, ?)',[
    nombre,
    stock
   ]);   
}
export async function update(nombre: string, stock: number, id_instrumento: string){
    return await client.execute(
    'UPDATE instrumento SET nombre = ?, stock = ? WHERE id_instrumento = ?',
    [
        nombre,
        stock,
        id_instrumento
    ],
    );  
}
export async function remove(id_instrumento : string){
    return await client.execute('DELETE FROM instrumento WHERE id_instrumento = ?', [id_instrumento]);
    
}
