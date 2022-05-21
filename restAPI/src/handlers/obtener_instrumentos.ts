import { search } from "../repository/instrumento.ts";


export async function obtener_instrumentos (ctx: any) {
    try {
        const result = await search();
        ctx.response.body = result.rows
    } catch (error) {
        console.log(error);
    }
    
}


