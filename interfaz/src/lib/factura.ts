
export type Factura = {
  Documentos: {
    FacturaElectronicaXML: {
      Encabezado: {
        TipoDoc: string;
        CondicionVenta: string;
        Sucursal: string;
        Terminal: string;
        Moneda: string;
        SituacionEnvio: string;
        CodigoActividad: string;
        MediosPago: {
          TiposMedioPago: string;
        };
        Receptor: {
          tipoidreceptor: string;
          nombrereceptor: string;
          correoreceptor: string;
          numdoc: string;
          Ubicacion: {
            provincia: string;
            canton: string;
            distrito: string;
            otrassenas: string;
          };
        };
        Emisor: {
          numcuentaemisor: string;
        };
      };
      Detalle: {
        preciounitario: string;
        cantidad: string;
        Linea: {
          unidadmedida: string;
          preciounitario: string;
          detallemerc: string;
          codigocabyss: string;
          Impuestos: {
            Impuesto: {
              tipo_iva: string;
              tarifa_iva: string;
              porcentaje_iva: string;
              monto_iva: number;
              Exoneracion: {
                motivo_exoneracion: string;
                num_doc_exo: string;
                institucion: string;
                fecha_exo: string;
                porcentaje_exo: number;
                monto_exonerado: number;
              };
            };
          };
        };
      };
      Totales: {
        totalServGravados: number;
        totalServExentos: number;
        totalServExonerados: number;
        totalMercanciasGravadas: number;
        totalMercanciasExentas: number;
        totalMercanciasExoneradas: number;
        totalGravado: number;
        totalExento: number;
        totalExonerado: number;
        totalOtrosCargos: number;
        totalIVADevuelto: number;
        totalVenta: number;
        totalVentaNeta: number;
        totalDescuentos: number;
        totalImpuesto: number;
        totalNoSujeto: number;
        totalServNoSujetos: number;
        totalMercanciaNoSujeta: number;
        totalImpuestoAsumidoEmisor: number;
        totalComprobante: number;
      };
      Extra: {
        EsVersion4_4: boolean;
      };
    };
  };
};

export function NuevaFactura(): Factura
{
    return {
        Documentos:{
            FacturaElectronicaXML:{

                Encabezado:{
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
                    Receptor:{
                        tipoidreceptor: "",
                        nombrereceptor: "",
                        correoreceptor: "",
                        numdoc: "",
                        Ubicacion:{
                            provincia: "",
                            canton: "",
                            distrito: "",
                            otrassenas: "",
                        },
                    },
                    Emisor:{
                        numcuentaemisor: "",
                    }
                },
                Detalle:{
                    preciounitario: "",
                    cantidad: "",
                    Linea:{
                        unidadmedida: "",
                        preciounitario: "",
                        detallemerc: "",
                        codigocabyss: "",

                        Impuestos:{
                            Impuesto:{
                                 tipo_iva: "",
                                tarifa_iva: "",
                                porcentaje_iva:"",
                                monto_iva: 0,
                                Exoneracion:{
                                    motivo_exoneracion: "",
                                    num_doc_exo: "",
                                    institucion: "",
                                    fecha_exo: "",
                                    porcentaje_exo: 0,
                                    monto_exonerado: 0,
                                }
                            },
                        }
                    }
                },
                Totales:{
                    totalServGravados: 0,
                    totalServExentos: 0,
                    totalServExonerados: 0,
                    totalMercanciasGravadas: 0,
                    totalMercanciasExentas: 0,
                    totalMercanciasExoneradas: 0,
                    totalGravado: 0,
                    totalExento: 0,
                    totalExonerado: 0,
                    totalOtrosCargos: 0,
                    totalIVADevuelto: 0,
                    totalVenta: 0,
                    totalVentaNeta: 0,
                    totalDescuentos: 0,
                    totalImpuesto: 0,
                    totalNoSujeto: 0,
                    totalServNoSujetos: 0,
                    totalMercanciaNoSujeta: 0,
                    totalImpuestoAsumidoEmisor: 0,
                    totalComprobante: 0
                },
                Extra:{
                    EsVersion4_4: true
                }
            }
        }
    }
}