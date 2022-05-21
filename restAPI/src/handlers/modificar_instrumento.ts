import { update } from '../repository/instrumento.ts'
import * as does_instrument_exists from '../libs/does_instrument_exists.ts'

export async function modificar_instrumento({request, params , response}: any) {
    const instrumento_exists = await does_instrument_exists.find_by_id(params.id);

    if (instrumento_exists) {

        const body = request.body();
        const instrumento: any = await body.value;

        response.status =200;
        response.body = await update(instrumento.nombre, instrumento.stock, params.id)
        
    } else {
        response.status = 404;
        response.body = {message: 'instrumento not found'}
    }
    
}


