// Original file: protos/proto/gRPC.proto

import type { Timestamp as _google_protobuf_Timestamp, Timestamp__Output as _google_protobuf_Timestamp__Output } from '../google/protobuf/Timestamp';

/**
 * Mensagem de requisição
 */
export interface Requisicao {
  'checkInDate'?: (_google_protobuf_Timestamp | null);
  'checkOutDate'?: (_google_protobuf_Timestamp | null);
  'origin'?: (string);
  'destination'?: (string);
  'numberOfPeople'?: (number);
  '_checkOutDate'?: "checkOutDate";
}

/**
 * Mensagem de requisição
 */
export interface Requisicao__Output {
  'checkInDate': (_google_protobuf_Timestamp__Output | null);
  'checkOutDate'?: (_google_protobuf_Timestamp__Output | null);
  'origin': (string);
  'destination': (string);
  'numberOfPeople': (number);
}
