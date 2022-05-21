import { Router } from "https://deno.land/x/oak@v10.5.1/mod.ts";
import { obtener_instrumento_almacen } from "./handlers/get_by_almacen.ts";
import { obtener_stock } from "./handlers/get_stock.ts"
import { agregar_instrumento } from "./handlers/agregar_instrumento.ts";
import { borrar_instrumento } from "./handlers/borrar_instrumento.ts";
import { obtener_instrumentos } from "./handlers/obtener_instrumentos.ts";
import { obtener_instrumento } from "./handlers/obtener_instrumento.ts";
import { modificar_instrumento } from "./handlers/modificar_instrumento.ts";
import { welcome } from "./handlers/welcome.ts";
import { sucursal } from "./handlers/sucursal.ts";
const router = new Router();

router
  .get("/", welcome)
  .get("/sucursal", sucursal)
  .get("/instrumento", obtener_instrumentos)
  .get("/instrumento/:id", obtener_instrumento)
  .get("/get_by_almacen/:id", obtener_instrumento_almacen)
  .get("/get_stock", obtener_stock)
  .post("/instrumento", agregar_instrumento)
  .put("/instrumento/:id", modificar_instrumento)
  .delete("/instrumento/:id", borrar_instrumento);
export default router;
