export class Factura {
    // atributos de la clase
    nombre: string | null;
    cedula: string | null;
    correo: string | null;
    telefono: string | null;
    provincia: string | null;
    canton: string | null;
    distrito: string | null;
    otras_senas: string | null;
    codigo: string | null;
    cantidad: number | null;
    descripcion: string | null;
    precio: number | null;
    impuesto: number | null;
    total: number | null;

    constructor() {
        this.nombre = null;
        this.cedula = null;
        this.correo = null;
        this.telefono = null;
        this.provincia = null;
        this.canton = null;
        this.distrito = null;
        this.otras_senas = null;
        this.codigo = null;
        this.cantidad = null;
        this.descripcion = null;
        this.precio = null;
        this.impuesto = null;
        this.total = null;
    }
}