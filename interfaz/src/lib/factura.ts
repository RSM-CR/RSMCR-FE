
export type Factura = {
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
          TipoIdReceptor: string;
          NombreReceptor: string;
          CorreoReceptor: string;
          NumDoc: string;
          Ubicacion: {
            Provincia: string;
            Canton: string;
            Distrito: string;
            OtrasSenas: string;
          };
        };
        Emisor: {
          NumCuentaEmisor: string;
        };
      };
      Detalle: {
        PrecioUnitario: string;
        Cantidad: string;
        Linea: {
          UnidadMedida: string;
          PrecioUnitario: string;
          DetalleMerc: string;
          CodigoCabyss: string;
          Impuestos: {
            Impuesto: {
              Tipo_Iva: string;
              Tarifa_Iva: string;
              Porcentaje_Iva: string;
              Monto_Iva: number;
              Exoneracion: {
                Motivo_Exoneracion: string;
                Num_Doc_Exo: string;
                Institucion: string;
                Fecha_Exo: string;
                Porcentaje_Exo: number;
                Monto_Exonerado: number;
              };
            };
          };
        };
      };
      Totales: {
        TotalesServGravados: number;
        TotalServExentos: number;
        TotalServExonerados: number;
        TotalMercanciasGravadas: number;
        TotalMercanciasExentas: number;
        TotalMercanciasExoneradas: number;
        TotalGravado: number;
        TotalExento: number;
        TotalExonerado: number;
        TotalOtrosCargos: number;
        TotalIVADevuelto: number;
        TotalVenta: number;
        TotalVentaNeta: number;
        TotalDescuentos: number;
        TotalImpuesto: number;
        TotalNoSujeto: number;
        TotalServNoSujetos: number;
        TotalMercanciaNoSujeta: number;
        TotalImpuestoAsumidoEmisor: number;
        TotalComprobante: number;
      };
      Extra: {
        EsVersion4_4: boolean;
      };
    };

export function NuevaFactura(): Factura
{
    return {
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
                        TipoIdReceptor: "",
                        NombreReceptor: "",
                        CorreoReceptor: "",
                        NumDoc: "",
                        Ubicacion:{
                            Provincia: "",
                            Canton: "",
                            Distrito: "",
                            OtrasSenas: "",
                        },
                    },
                    Emisor:{
                        NumCuentaEmisor: "",
                    }
                },
                Detalle:{
                    PrecioUnitario: "",
                    Cantidad: "",
                    Linea:{
                        UnidadMedida: "",
                        PrecioUnitario: "",
                        DetalleMerc: "",
                        CodigoCabyss: "",

                        Impuestos:{
                            Impuesto:{
                                 Tipo_Iva: "",
                                 Tarifa_Iva: "",
                                 Porcentaje_Iva:"",
                                 Monto_Iva: 0,
                                 Exoneracion:{
                                    Motivo_Exoneracion: "",
                                    Num_Doc_Exo: "",
                                    Institucion: "",
                                    Fecha_Exo: "",
                                    Porcentaje_Exo: 0,
                                    Monto_Exonerado: 0,
                                }
                            },
                        }
                    }
                },
                Totales:{
                    TotalesServGravados: 0,
                    TotalServExentos: 0,
                    TotalServExonerados: 0,
                    TotalMercanciasGravadas: 0,
                    TotalMercanciasExentas: 0,
                    TotalMercanciasExoneradas: 0,
                    TotalGravado: 0,
                    TotalExento: 0,
                    TotalExonerado: 0,
                    TotalOtrosCargos: 0,
                    TotalIVADevuelto: 0,
                    TotalVenta: 0,
                    TotalVentaNeta: 0,
                    TotalDescuentos: 0,
                    TotalImpuesto: 0,
                    TotalNoSujeto: 0,
                    TotalServNoSujetos: 0,
                    TotalMercanciaNoSujeta: 0,
                    TotalImpuestoAsumidoEmisor: 0,
                    TotalComprobante: 0
                },
                Extra:{
                    EsVersion4_4: true
                }
            }
        }