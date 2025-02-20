// Original file: protos/proto/gRPC.proto


/**
 * Mensagem de resposta
 */
export interface Resposta {
  'success'?: (boolean);
  'message'?: (string);
  'reservationId'?: (string);
  '_reservationId'?: "reservationId";
}

/**
 * Mensagem de resposta
 */
export interface Resposta__Output {
  'success': (boolean);
  'message': (string);
  'reservationId'?: (string);
}
