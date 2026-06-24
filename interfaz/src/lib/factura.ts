// No sé si lo vamos a ocupar por el nuevo modelo con objetos JSON
// export class Factura {
//     // atributos de la clase
//     nombre: string | null;
//     cedula: string | null;
//     correo: string | null;
//     telefono: string | null;
//     provincia: string | null;
//     canton: string | null;
//     distrito: string | null;
//     otras_senas: string | null;
//     codigo: string | null;
//     cantidad: number | null;
//     descripcion: string | null;
//     precio: number | null;
//     impuesto: number | null;
//     total: number | null;

//     constructor() {
//         this.nombre = null;
//         this.cedula = null;
//         this.correo = null;
//         this.telefono = null;
//         this.provincia = null;
//         this.canton = null;
//         this.distrito = null;
//         this.otras_senas = null;
//         this.codigo = null;
//         this.cantidad = null;
//         this.descripcion = null;
//         this.precio = null;
//         this.impuesto = null;
//         this.total = null;
//     }
// }

export type Factura =
{
    TipoDoc: string;
    CondicionVenta: string;
    Sucursal: string;
    Terminal: string;
    Moneda: string;
    SituacionEnvio: string;
    CodigoActividad: string;
    MediosPago: {
        TiposMedioPago: string
    }
    tipoidreceptor: string;
    numcuentaemisor: string;
    unidadmedida: string;
    provincia: string;
    canton: string;
    distrito: string;
    otrassenas: string;
    numdoc: string;
    tipo_iva: string;
    tarifa_iva: string;
    porcentaje_iva: number;
    monto_iva: number;
    motivo_exoneracion: string;
    num_doc_exo: string;
    institucion: string;
    fecha_exo: string;
    porcentaje_exo: number;
    monto_exonerado: number;
}

export function NuevaFactura(): Factura
{
    return {
        TipoDoc: "",
        CondicionVenta: "",
        Sucursal: "",
        Terminal: "",
        Moneda: "",
        SituacionEnvio: "",
        CodigoActividad: "",
        MediosPago: {
        TiposMedioPago: ""
        },
        tipoidreceptor: "",
        numcuentaemisor: "",
        unidadmedida: "",
        provincia: "",
        canton: "",
        distrito: "",
        otrassenas: "",
        numdoc: "",
        tipo_iva: "",
        tarifa_iva:"",
        porcentaje_iva: 0,
        monto_iva: 0,
        motivo_exoneracion: "",
        num_doc_exo: "",
        institucion: "",
        fecha_exo: "",
        porcentaje_exo: 0,
        monto_exonerado: 0

    }
}