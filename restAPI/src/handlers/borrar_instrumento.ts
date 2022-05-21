import { remove } from '../repository/instrumento.ts';
import * as does_instrument_exists from '../libs/does_instrument_exists.ts';


export async function borrar_instrumento({params, response}: any) {
    const user_exists = await does_instrument_exists.find_by_id(params.id);

    if (user_exists) {
        response.status = 200;
        response.body = await remove(params.id);
        
    } else {
        response.status = 404;
        response.body = {message: 'User not found'}
    }

}


