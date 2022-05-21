import { Router } from "https://deno.land/x/oak@v10.5.1/mod.ts";

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
  .post("/instrumento", agregar_instrumento)
  .put("/instrumento/:id", modificar_instrumento)
  .delete("/instrumento/:id", borrar_instrumento);
export default router;
