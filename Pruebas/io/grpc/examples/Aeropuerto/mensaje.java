// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: Aeropuerto.proto

package io.grpc.examples.Aeropuerto;

/**
 * Protobuf type {@code Aeropuerto.mensaje}
 */
public  final class mensaje extends
    com.google.protobuf.GeneratedMessageV3 implements
    // @@protoc_insertion_point(message_implements:Aeropuerto.mensaje)
    mensajeOrBuilder {
private static final long serialVersionUID = 0L;
  // Use mensaje.newBuilder() to construct.
  private mensaje(com.google.protobuf.GeneratedMessageV3.Builder<?> builder) {
    super(builder);
  }
  private mensaje() {
    altura_ = 0;
  }

  @java.lang.Override
  public final com.google.protobuf.UnknownFieldSet
  getUnknownFields() {
    return this.unknownFields;
  }
  private mensaje(
      com.google.protobuf.CodedInputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    this();
    if (extensionRegistry == null) {
      throw new java.lang.NullPointerException();
    }
    int mutable_bitField0_ = 0;
    com.google.protobuf.UnknownFieldSet.Builder unknownFields =
        com.google.protobuf.UnknownFieldSet.newBuilder();
    try {
      boolean done = false;
      while (!done) {
        int tag = input.readTag();
        switch (tag) {
          case 0:
            done = true;
            break;
          case 8: {

            altura_ = input.readInt32();
            break;
          }
          default: {
            if (!parseUnknownFieldProto3(
                input, unknownFields, extensionRegistry, tag)) {
              done = true;
            }
            break;
          }
        }
      }
    } catch (com.google.protobuf.InvalidProtocolBufferException e) {
      throw e.setUnfinishedMessage(this);
    } catch (java.io.IOException e) {
      throw new com.google.protobuf.InvalidProtocolBufferException(
          e).setUnfinishedMessage(this);
    } finally {
      this.unknownFields = unknownFields.build();
      makeExtensionsImmutable();
    }
  }
  public static final com.google.protobuf.Descriptors.Descriptor
      getDescriptor() {
    return io.grpc.examples.Aeropuerto.AeropuertoProto.internal_static_Aeropuerto_mensaje_descriptor;
  }

  @java.lang.Override
  protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internalGetFieldAccessorTable() {
    return io.grpc.examples.Aeropuerto.AeropuertoProto.internal_static_Aeropuerto_mensaje_fieldAccessorTable
        .ensureFieldAccessorsInitialized(
            io.grpc.examples.Aeropuerto.mensaje.class, io.grpc.examples.Aeropuerto.mensaje.Builder.class);
  }

  public static final int ALTURA_FIELD_NUMBER = 1;
  private int altura_;
  /**
   * <code>int32 altura = 1;</code>
   */
  public int getAltura() {
    return altura_;
  }

  private byte memoizedIsInitialized = -1;
  @java.lang.Override
  public final boolean isInitialized() {
    byte isInitialized = memoizedIsInitialized;
    if (isInitialized == 1) return true;
    if (isInitialized == 0) return false;

    memoizedIsInitialized = 1;
    return true;
  }

  @java.lang.Override
  public void writeTo(com.google.protobuf.CodedOutputStream output)
                      throws java.io.IOException {
    if (altura_ != 0) {
      output.writeInt32(1, altura_);
    }
    unknownFields.writeTo(output);
  }

  @java.lang.Override
  public int getSerializedSize() {
    int size = memoizedSize;
    if (size != -1) return size;

    size = 0;
    if (altura_ != 0) {
      size += com.google.protobuf.CodedOutputStream
        .computeInt32Size(1, altura_);
    }
    size += unknownFields.getSerializedSize();
    memoizedSize = size;
    return size;
  }

  @java.lang.Override
  public boolean equals(final java.lang.Object obj) {
    if (obj == this) {
     return true;
    }
    if (!(obj instanceof io.grpc.examples.Aeropuerto.mensaje)) {
      return super.equals(obj);
    }
    io.grpc.examples.Aeropuerto.mensaje other = (io.grpc.examples.Aeropuerto.mensaje) obj;

    boolean result = true;
    result = result && (getAltura()
        == other.getAltura());
    result = result && unknownFields.equals(other.unknownFields);
    return result;
  }

  @java.lang.Override
  public int hashCode() {
    if (memoizedHashCode != 0) {
      return memoizedHashCode;
    }
    int hash = 41;
    hash = (19 * hash) + getDescriptor().hashCode();
    hash = (37 * hash) + ALTURA_FIELD_NUMBER;
    hash = (53 * hash) + getAltura();
    hash = (29 * hash) + unknownFields.hashCode();
    memoizedHashCode = hash;
    return hash;
  }

  public static io.grpc.examples.Aeropuerto.mensaje parseFrom(
      java.nio.ByteBuffer data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseFrom(
      java.nio.ByteBuffer data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseFrom(
      com.google.protobuf.ByteString data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseFrom(
      com.google.protobuf.ByteString data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseFrom(byte[] data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseFrom(
      byte[] data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseDelimitedFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseDelimitedFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input, extensionRegistry);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseFrom(
      com.google.protobuf.CodedInputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static io.grpc.examples.Aeropuerto.mensaje parseFrom(
      com.google.protobuf.CodedInputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }

  @java.lang.Override
  public Builder newBuilderForType() { return newBuilder(); }
  public static Builder newBuilder() {
    return DEFAULT_INSTANCE.toBuilder();
  }
  public static Builder newBuilder(io.grpc.examples.Aeropuerto.mensaje prototype) {
    return DEFAULT_INSTANCE.toBuilder().mergeFrom(prototype);
  }
  @java.lang.Override
  public Builder toBuilder() {
    return this == DEFAULT_INSTANCE
        ? new Builder() : new Builder().mergeFrom(this);
  }

  @java.lang.Override
  protected Builder newBuilderForType(
      com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
    Builder builder = new Builder(parent);
    return builder;
  }
  /**
   * Protobuf type {@code Aeropuerto.mensaje}
   */
  public static final class Builder extends
      com.google.protobuf.GeneratedMessageV3.Builder<Builder> implements
      // @@protoc_insertion_point(builder_implements:Aeropuerto.mensaje)
      io.grpc.examples.Aeropuerto.mensajeOrBuilder {
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return io.grpc.examples.Aeropuerto.AeropuertoProto.internal_static_Aeropuerto_mensaje_descriptor;
    }

    @java.lang.Override
    protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return io.grpc.examples.Aeropuerto.AeropuertoProto.internal_static_Aeropuerto_mensaje_fieldAccessorTable
          .ensureFieldAccessorsInitialized(
              io.grpc.examples.Aeropuerto.mensaje.class, io.grpc.examples.Aeropuerto.mensaje.Builder.class);
    }

    // Construct using io.grpc.examples.Aeropuerto.mensaje.newBuilder()
    private Builder() {
      maybeForceBuilderInitialization();
    }

    private Builder(
        com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
      super(parent);
      maybeForceBuilderInitialization();
    }
    private void maybeForceBuilderInitialization() {
      if (com.google.protobuf.GeneratedMessageV3
              .alwaysUseFieldBuilders) {
      }
    }
    @java.lang.Override
    public Builder clear() {
      super.clear();
      altura_ = 0;

      return this;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.Descriptor
        getDescriptorForType() {
      return io.grpc.examples.Aeropuerto.AeropuertoProto.internal_static_Aeropuerto_mensaje_descriptor;
    }

    @java.lang.Override
    public io.grpc.examples.Aeropuerto.mensaje getDefaultInstanceForType() {
      return io.grpc.examples.Aeropuerto.mensaje.getDefaultInstance();
    }

    @java.lang.Override
    public io.grpc.examples.Aeropuerto.mensaje build() {
      io.grpc.examples.Aeropuerto.mensaje result = buildPartial();
      if (!result.isInitialized()) {
        throw newUninitializedMessageException(result);
      }
      return result;
    }

    @java.lang.Override
    public io.grpc.examples.Aeropuerto.mensaje buildPartial() {
      io.grpc.examples.Aeropuerto.mensaje result = new io.grpc.examples.Aeropuerto.mensaje(this);
      result.altura_ = altura_;
      onBuilt();
      return result;
    }

    @java.lang.Override
    public Builder clone() {
      return (Builder) super.clone();
    }
    @java.lang.Override
    public Builder setField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        java.lang.Object value) {
      return (Builder) super.setField(field, value);
    }
    @java.lang.Override
    public Builder clearField(
        com.google.protobuf.Descriptors.FieldDescriptor field) {
      return (Builder) super.clearField(field);
    }
    @java.lang.Override
    public Builder clearOneof(
        com.google.protobuf.Descriptors.OneofDescriptor oneof) {
      return (Builder) super.clearOneof(oneof);
    }
    @java.lang.Override
    public Builder setRepeatedField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        int index, java.lang.Object value) {
      return (Builder) super.setRepeatedField(field, index, value);
    }
    @java.lang.Override
    public Builder addRepeatedField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        java.lang.Object value) {
      return (Builder) super.addRepeatedField(field, value);
    }
    @java.lang.Override
    public Builder mergeFrom(com.google.protobuf.Message other) {
      if (other instanceof io.grpc.examples.Aeropuerto.mensaje) {
        return mergeFrom((io.grpc.examples.Aeropuerto.mensaje)other);
      } else {
        super.mergeFrom(other);
        return this;
      }
    }

    public Builder mergeFrom(io.grpc.examples.Aeropuerto.mensaje other) {
      if (other == io.grpc.examples.Aeropuerto.mensaje.getDefaultInstance()) return this;
      if (other.getAltura() != 0) {
        setAltura(other.getAltura());
      }
      this.mergeUnknownFields(other.unknownFields);
      onChanged();
      return this;
    }

    @java.lang.Override
    public final boolean isInitialized() {
      return true;
    }

    @java.lang.Override
    public Builder mergeFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      io.grpc.examples.Aeropuerto.mensaje parsedMessage = null;
      try {
        parsedMessage = PARSER.parsePartialFrom(input, extensionRegistry);
      } catch (com.google.protobuf.InvalidProtocolBufferException e) {
        parsedMessage = (io.grpc.examples.Aeropuerto.mensaje) e.getUnfinishedMessage();
        throw e.unwrapIOException();
      } finally {
        if (parsedMessage != null) {
          mergeFrom(parsedMessage);
        }
      }
      return this;
    }

    private int altura_ ;
    /**
     * <code>int32 altura = 1;</code>
     */
    public int getAltura() {
      return altura_;
    }
    /**
     * <code>int32 altura = 1;</code>
     */
    public Builder setAltura(int value) {
      
      altura_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>int32 altura = 1;</code>
     */
    public Builder clearAltura() {
      
      altura_ = 0;
      onChanged();
      return this;
    }
    @java.lang.Override
    public final Builder setUnknownFields(
        final com.google.protobuf.UnknownFieldSet unknownFields) {
      return super.setUnknownFieldsProto3(unknownFields);
    }

    @java.lang.Override
    public final Builder mergeUnknownFields(
        final com.google.protobuf.UnknownFieldSet unknownFields) {
      return super.mergeUnknownFields(unknownFields);
    }


    // @@protoc_insertion_point(builder_scope:Aeropuerto.mensaje)
  }

  // @@protoc_insertion_point(class_scope:Aeropuerto.mensaje)
  private static final io.grpc.examples.Aeropuerto.mensaje DEFAULT_INSTANCE;
  static {
    DEFAULT_INSTANCE = new io.grpc.examples.Aeropuerto.mensaje();
  }

  public static io.grpc.examples.Aeropuerto.mensaje getDefaultInstance() {
    return DEFAULT_INSTANCE;
  }

  private static final com.google.protobuf.Parser<mensaje>
      PARSER = new com.google.protobuf.AbstractParser<mensaje>() {
    @java.lang.Override
    public mensaje parsePartialFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return new mensaje(input, extensionRegistry);
    }
  };

  public static com.google.protobuf.Parser<mensaje> parser() {
    return PARSER;
  }

  @java.lang.Override
  public com.google.protobuf.Parser<mensaje> getParserForType() {
    return PARSER;
  }

  @java.lang.Override
  public io.grpc.examples.Aeropuerto.mensaje getDefaultInstanceForType() {
    return DEFAULT_INSTANCE;
  }

}

