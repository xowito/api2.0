import { searchByAlmacen } from '../repository/instrumento.ts'

export async function obtener_stock(ctx: any) {


    try {
        const result = await searchByAlmacen();
        ctx.response.body = result.rows
    } catch (error) {
        console.log(error);
    }
}