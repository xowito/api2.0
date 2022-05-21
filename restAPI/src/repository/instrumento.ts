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
interface ParamsByAlmacen{
    id? : string | number
}
export async function searchByAlmacen(params: ParamsByAlmacen = {}){
    const isSpecific =  Object.keys(params).length !== 0;

    if (isSpecific) {
        return await client.execute('SELECT i.id_instrumento, i.nombre, i.precio, i.stock, i.created_at, i.updated_at, almacen.nombre_almacen  from instrumento i JOIN almacen almacen ON(i.id_almacen = almacen.id_almacen) WHERE i.id_almacen = ?', [params.id]);
    } else {
        return await client.execute('SELECT instrumento.id_instrumento, instrumento.nombre, instrumento.stock, instrumento.precio, almacen.id_almacen, almacen.nombre_almacen FROM instrumento LEFT JOIN almacen ON instrumento.id_almacen = almacen.id_almacen');
    }
    

}




interface InsertParams {
    nombre: string,
    stock: number,
    precio: number
}
export async function insert({nombre, stock, precio}: InsertParams){
   return await client.execute('INSERT INTO instrumento(nombre, stock, precio) VALUES (?, ?, ?)',[
    nombre,
    stock,
    precio
   ]);   
}
export async function update(nombre: string, stock: number, precio: number, id_instrumento: string){
    return await client.execute(
    'UPDATE instrumento SET nombre = ?, stock = ?, precio = ? WHERE id_instrumento = ?',
    [
        nombre,
        stock,
        precio,
        id_instrumento
    ],
    );  
}
export async function remove(id_instrumento : string){
    return await client.execute('DELETE FROM instrumento WHERE id_instrumento = ?', [id_instrumento]);
    
}
