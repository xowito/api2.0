import { Application } from "https://deno.land/x/oak@v10.5.1/mod.ts";
import router from './routes.ts';
import { oakCors } from "https://deno.land/x/cors@v1.2.2/mod.ts";
const app = new Application();
app.use(oakCors({
    origin: "*",
    optionsSuccessStatus: 200,
    
  }),);
app.use(router.routes(),
);


await app.listen({port:3000})

const githubResponse = async (): Promise<any> => {
    const response = await fetch("http://localhost:3000", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET"
        },
    });
    return response.json(); // For JSON Response
    //   return response.text(); // For HTML or Text Response
}

console.log(await githubResponse());