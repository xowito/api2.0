import { insert } from '../repository/instrumento.ts'

export async function agregar_instrumento({response, request}: any) {
   
    const body = await request.body();
    const instrumento = await body.value;
    
    if (instrumento.hasOwnProperty('nombre') && instrumento.hasOwnProperty('stock')){
        
        response.status = 200;
        response.body = await insert(instrumento);
    } else {
        response.body = {message: 'Invalid request'};
        response.status = 404;
    }


    response.body = 'adding instrumento';
}