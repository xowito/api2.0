import { search } from '../repository/instrumento.ts'
import * as does_instrument_exists from '../libs/does_instrument_exists.ts'

export async function obtener_instrumento({response, params}: any) {


    const instrument_exists = await does_instrument_exists.find_by_id(params.id)

    if (instrument_exists) {
        const result = await search(params);
        response.status = 200;
        response.body = result.rows;
    } else {
        response.status = 404;
        response.body = {message: 'instrumento no encontrado'}
    }
}


