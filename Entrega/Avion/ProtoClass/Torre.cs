// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: Torre.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Aeropuerto {

  /// <summary>Holder for reflection information generated from Torre.proto</summary>
  public static partial class TorreReflection {

    #region Descriptor
    /// <summary>File descriptor for Torre.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static TorreReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CgtUb3JyZS5wcm90bxIKQWVyb3B1ZXJ0byIdCglQaXN0YV9EZXMSEAoISWRf",
            "YXZpb24YASABKAkitgEKCFJlc3BfRGVzEh0KFUF1dG9yaXphY2lvbl9kZXNw",
            "ZWd1ZRgBIAEoCBIWCg5QaXN0YV9kZXNwZWd1ZRgCIAEoBRIXCg9BbHR1cmFf",
            "ZGVzcGVndWUYAyABKAUSGQoRUG9zaWNpb25fZGVzcGVndWUYBCABKAUSGQoR",
            "QW50ZXJpb3JfZGVzcGVndWUYBSABKAkSEgoKSXBfZGVzdGlubxgGIAEoCRIQ",
            "CghJZF9hdmlvbhgHIAEoCSIcCghQaXN0YV9BdBIQCghJZF9hdmlvbhgBIAEo",
            "CSKrAQoHUmVzcF9BdBIfChdBdXRvcml6YWNpb25fYXRlcnJpemFqZRgBIAEo",
            "CBIYChBQaXN0YV9hdGVycml6YWplGAIgASgFEhkKEUFsdHVyYV9hdGVycml6",
            "YWplGAMgASgFEhsKE1Bvc2ljaW9uX2F0ZXJyaXphamUYBCABKAUSGwoTQW50",
            "ZXJpb3JfYXRlcnJpemFqZRgFIAEoCRIQCghJZF9hdmlvbhgGIAEoCTJMCghE",
            "ZXNwZWd1ZRJACg9lbnZpYXJfZGVzcGVndWUSFS5BZXJvcHVlcnRvLlBpc3Rh",
            "X0RlcxoULkFlcm9wdWVydG8uUmVzcF9EZXMiADJOCgpBdGVycml6YWplEkAK",
            "EWVudmlhcl9hdGVycml6YWplEhQuQWVyb3B1ZXJ0by5QaXN0YV9BdBoTLkFl",
            "cm9wdWVydG8uUmVzcF9BdCIAQjYKG2lvLmdycGMuZXhhbXBsZXMuQWVyb3B1",
            "ZXJ0b0IPQWVyb3B1ZXJ0b1Byb3RvUAGiAgNITFdiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Aeropuerto.Pista_Des), global::Aeropuerto.Pista_Des.Parser, new[]{ "IdAvion" }, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Aeropuerto.Resp_Des), global::Aeropuerto.Resp_Des.Parser, new[]{ "AutorizacionDespegue", "PistaDespegue", "AlturaDespegue", "PosicionDespegue", "AnteriorDespegue", "IpDestino", "IdAvion" }, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Aeropuerto.Pista_At), global::Aeropuerto.Pista_At.Parser, new[]{ "IdAvion" }, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Aeropuerto.Resp_At), global::Aeropuerto.Resp_At.Parser, new[]{ "AutorizacionAterrizaje", "PistaAterrizaje", "AlturaAterrizaje", "PosicionAterrizaje", "AnteriorAterrizaje", "IdAvion" }, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class Pista_Des : pb::IMessage<Pista_Des> {
    private static readonly pb::MessageParser<Pista_Des> _parser = new pb::MessageParser<Pista_Des>(() => new Pista_Des());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<Pista_Des> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Aeropuerto.TorreReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Pista_Des() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Pista_Des(Pista_Des other) : this() {
      idAvion_ = other.idAvion_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Pista_Des Clone() {
      return new Pista_Des(this);
    }

    /// <summary>Field number for the "Id_avion" field.</summary>
    public const int IdAvionFieldNumber = 1;
    private string idAvion_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string IdAvion {
      get { return idAvion_; }
      set {
        idAvion_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as Pista_Des);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(Pista_Des other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (IdAvion != other.IdAvion) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (IdAvion.Length != 0) hash ^= IdAvion.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (IdAvion.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(IdAvion);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (IdAvion.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(IdAvion);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(Pista_Des other) {
      if (other == null) {
        return;
      }
      if (other.IdAvion.Length != 0) {
        IdAvion = other.IdAvion;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            IdAvion = input.ReadString();
            break;
          }
        }
      }
    }

  }

  public sealed partial class Resp_Des : pb::IMessage<Resp_Des> {
    private static readonly pb::MessageParser<Resp_Des> _parser = new pb::MessageParser<Resp_Des>(() => new Resp_Des());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<Resp_Des> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Aeropuerto.TorreReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Resp_Des() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Resp_Des(Resp_Des other) : this() {
      autorizacionDespegue_ = other.autorizacionDespegue_;
      pistaDespegue_ = other.pistaDespegue_;
      alturaDespegue_ = other.alturaDespegue_;
      posicionDespegue_ = other.posicionDespegue_;
      anteriorDespegue_ = other.anteriorDespegue_;
      ipDestino_ = other.ipDestino_;
      idAvion_ = other.idAvion_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Resp_Des Clone() {
      return new Resp_Des(this);
    }

    /// <summary>Field number for the "Autorizacion_despegue" field.</summary>
    public const int AutorizacionDespegueFieldNumber = 1;
    private bool autorizacionDespegue_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool AutorizacionDespegue {
      get { return autorizacionDespegue_; }
      set {
        autorizacionDespegue_ = value;
      }
    }

    /// <summary>Field number for the "Pista_despegue" field.</summary>
    public const int PistaDespegueFieldNumber = 2;
    private int pistaDespegue_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int PistaDespegue {
      get { return pistaDespegue_; }
      set {
        pistaDespegue_ = value;
      }
    }

    /// <summary>Field number for the "Altura_despegue" field.</summary>
    public const int AlturaDespegueFieldNumber = 3;
    private int alturaDespegue_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int AlturaDespegue {
      get { return alturaDespegue_; }
      set {
        alturaDespegue_ = value;
      }
    }

    /// <summary>Field number for the "Posicion_despegue" field.</summary>
    public const int PosicionDespegueFieldNumber = 4;
    private int posicionDespegue_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int PosicionDespegue {
      get { return posicionDespegue_; }
      set {
        posicionDespegue_ = value;
      }
    }

    /// <summary>Field number for the "Anterior_despegue" field.</summary>
    public const int AnteriorDespegueFieldNumber = 5;
    private string anteriorDespegue_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string AnteriorDespegue {
      get { return anteriorDespegue_; }
      set {
        anteriorDespegue_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "Ip_destino" field.</summary>
    public const int IpDestinoFieldNumber = 6;
    private string ipDestino_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string IpDestino {
      get { return ipDestino_; }
      set {
        ipDestino_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "Id_avion" field.</summary>
    public const int IdAvionFieldNumber = 7;
    private string idAvion_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string IdAvion {
      get { return idAvion_; }
      set {
        idAvion_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as Resp_Des);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(Resp_Des other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (AutorizacionDespegue != other.AutorizacionDespegue) return false;
      if (PistaDespegue != other.PistaDespegue) return false;
      if (AlturaDespegue != other.AlturaDespegue) return false;
      if (PosicionDespegue != other.PosicionDespegue) return false;
      if (AnteriorDespegue != other.AnteriorDespegue) return false;
      if (IpDestino != other.IpDestino) return false;
      if (IdAvion != other.IdAvion) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (AutorizacionDespegue != false) hash ^= AutorizacionDespegue.GetHashCode();
      if (PistaDespegue != 0) hash ^= PistaDespegue.GetHashCode();
      if (AlturaDespegue != 0) hash ^= AlturaDespegue.GetHashCode();
      if (PosicionDespegue != 0) hash ^= PosicionDespegue.GetHashCode();
      if (AnteriorDespegue.Length != 0) hash ^= AnteriorDespegue.GetHashCode();
      if (IpDestino.Length != 0) hash ^= IpDestino.GetHashCode();
      if (IdAvion.Length != 0) hash ^= IdAvion.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (AutorizacionDespegue != false) {
        output.WriteRawTag(8);
        output.WriteBool(AutorizacionDespegue);
      }
      if (PistaDespegue != 0) {
        output.WriteRawTag(16);
        output.WriteInt32(PistaDespegue);
      }
      if (AlturaDespegue != 0) {
        output.WriteRawTag(24);
        output.WriteInt32(AlturaDespegue);
      }
      if (PosicionDespegue != 0) {
        output.WriteRawTag(32);
        output.WriteInt32(PosicionDespegue);
      }
      if (AnteriorDespegue.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(AnteriorDespegue);
      }
      if (IpDestino.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(IpDestino);
      }
      if (IdAvion.Length != 0) {
        output.WriteRawTag(58);
        output.WriteString(IdAvion);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (AutorizacionDespegue != false) {
        size += 1 + 1;
      }
      if (PistaDespegue != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(PistaDespegue);
      }
      if (AlturaDespegue != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(AlturaDespegue);
      }
      if (PosicionDespegue != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(PosicionDespegue);
      }
      if (AnteriorDespegue.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(AnteriorDespegue);
      }
      if (IpDestino.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(IpDestino);
      }
      if (IdAvion.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(IdAvion);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(Resp_Des other) {
      if (other == null) {
        return;
      }
      if (other.AutorizacionDespegue != false) {
        AutorizacionDespegue = other.AutorizacionDespegue;
      }
      if (other.PistaDespegue != 0) {
        PistaDespegue = other.PistaDespegue;
      }
      if (other.AlturaDespegue != 0) {
        AlturaDespegue = other.AlturaDespegue;
      }
      if (other.PosicionDespegue != 0) {
        PosicionDespegue = other.PosicionDespegue;
      }
      if (other.AnteriorDespegue.Length != 0) {
        AnteriorDespegue = other.AnteriorDespegue;
      }
      if (other.IpDestino.Length != 0) {
        IpDestino = other.IpDestino;
      }
      if (other.IdAvion.Length != 0) {
        IdAvion = other.IdAvion;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 8: {
            AutorizacionDespegue = input.ReadBool();
            break;
          }
          case 16: {
            PistaDespegue = input.ReadInt32();
            break;
          }
          case 24: {
            AlturaDespegue = input.ReadInt32();
            break;
          }
          case 32: {
            PosicionDespegue = input.ReadInt32();
            break;
          }
          case 42: {
            AnteriorDespegue = input.ReadString();
            break;
          }
          case 50: {
            IpDestino = input.ReadString();
            break;
          }
          case 58: {
            IdAvion = input.ReadString();
            break;
          }
        }
      }
    }

  }

  public sealed partial class Pista_At : pb::IMessage<Pista_At> {
    private static readonly pb::MessageParser<Pista_At> _parser = new pb::MessageParser<Pista_At>(() => new Pista_At());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<Pista_At> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Aeropuerto.TorreReflection.Descriptor.MessageTypes[2]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Pista_At() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Pista_At(Pista_At other) : this() {
      idAvion_ = other.idAvion_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Pista_At Clone() {
      return new Pista_At(this);
    }

    /// <summary>Field number for the "Id_avion" field.</summary>
    public const int IdAvionFieldNumber = 1;
    private string idAvion_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string IdAvion {
      get { return idAvion_; }
      set {
        idAvion_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as Pista_At);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(Pista_At other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (IdAvion != other.IdAvion) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (IdAvion.Length != 0) hash ^= IdAvion.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (IdAvion.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(IdAvion);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (IdAvion.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(IdAvion);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(Pista_At other) {
      if (other == null) {
        return;
      }
      if (other.IdAvion.Length != 0) {
        IdAvion = other.IdAvion;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            IdAvion = input.ReadString();
            break;
          }
        }
      }
    }

  }

  public sealed partial class Resp_At : pb::IMessage<Resp_At> {
    private static readonly pb::MessageParser<Resp_At> _parser = new pb::MessageParser<Resp_At>(() => new Resp_At());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<Resp_At> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Aeropuerto.TorreReflection.Descriptor.MessageTypes[3]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Resp_At() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Resp_At(Resp_At other) : this() {
      autorizacionAterrizaje_ = other.autorizacionAterrizaje_;
      pistaAterrizaje_ = other.pistaAterrizaje_;
      alturaAterrizaje_ = other.alturaAterrizaje_;
      posicionAterrizaje_ = other.posicionAterrizaje_;
      anteriorAterrizaje_ = other.anteriorAterrizaje_;
      idAvion_ = other.idAvion_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Resp_At Clone() {
      return new Resp_At(this);
    }

    /// <summary>Field number for the "Autorizacion_aterrizaje" field.</summary>
    public const int AutorizacionAterrizajeFieldNumber = 1;
    private bool autorizacionAterrizaje_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool AutorizacionAterrizaje {
      get { return autorizacionAterrizaje_; }
      set {
        autorizacionAterrizaje_ = value;
      }
    }

    /// <summary>Field number for the "Pista_aterrizaje" field.</summary>
    public const int PistaAterrizajeFieldNumber = 2;
    private int pistaAterrizaje_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int PistaAterrizaje {
      get { return pistaAterrizaje_; }
      set {
        pistaAterrizaje_ = value;
      }
    }

    /// <summary>Field number for the "Altura_aterrizaje" field.</summary>
    public const int AlturaAterrizajeFieldNumber = 3;
    private int alturaAterrizaje_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int AlturaAterrizaje {
      get { return alturaAterrizaje_; }
      set {
        alturaAterrizaje_ = value;
      }
    }

    /// <summary>Field number for the "Posicion_aterrizaje" field.</summary>
    public const int PosicionAterrizajeFieldNumber = 4;
    private int posicionAterrizaje_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int PosicionAterrizaje {
      get { return posicionAterrizaje_; }
      set {
        posicionAterrizaje_ = value;
      }
    }

    /// <summary>Field number for the "Anterior_aterrizaje" field.</summary>
    public const int AnteriorAterrizajeFieldNumber = 5;
    private string anteriorAterrizaje_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string AnteriorAterrizaje {
      get { return anteriorAterrizaje_; }
      set {
        anteriorAterrizaje_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "Id_avion" field.</summary>
    public const int IdAvionFieldNumber = 6;
    private string idAvion_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string IdAvion {
      get { return idAvion_; }
      set {
        idAvion_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as Resp_At);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(Resp_At other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (AutorizacionAterrizaje != other.AutorizacionAterrizaje) return false;
      if (PistaAterrizaje != other.PistaAterrizaje) return false;
      if (AlturaAterrizaje != other.AlturaAterrizaje) return false;
      if (PosicionAterrizaje != other.PosicionAterrizaje) return false;
      if (AnteriorAterrizaje != other.AnteriorAterrizaje) return false;
      if (IdAvion != other.IdAvion) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (AutorizacionAterrizaje != false) hash ^= AutorizacionAterrizaje.GetHashCode();
      if (PistaAterrizaje != 0) hash ^= PistaAterrizaje.GetHashCode();
      if (AlturaAterrizaje != 0) hash ^= AlturaAterrizaje.GetHashCode();
      if (PosicionAterrizaje != 0) hash ^= PosicionAterrizaje.GetHashCode();
      if (AnteriorAterrizaje.Length != 0) hash ^= AnteriorAterrizaje.GetHashCode();
      if (IdAvion.Length != 0) hash ^= IdAvion.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (AutorizacionAterrizaje != false) {
        output.WriteRawTag(8);
        output.WriteBool(AutorizacionAterrizaje);
      }
      if (PistaAterrizaje != 0) {
        output.WriteRawTag(16);
        output.WriteInt32(PistaAterrizaje);
      }
      if (AlturaAterrizaje != 0) {
        output.WriteRawTag(24);
        output.WriteInt32(AlturaAterrizaje);
      }
      if (PosicionAterrizaje != 0) {
        output.WriteRawTag(32);
        output.WriteInt32(PosicionAterrizaje);
      }
      if (AnteriorAterrizaje.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(AnteriorAterrizaje);
      }
      if (IdAvion.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(IdAvion);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (AutorizacionAterrizaje != false) {
        size += 1 + 1;
      }
      if (PistaAterrizaje != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(PistaAterrizaje);
      }
      if (AlturaAterrizaje != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(AlturaAterrizaje);
      }
      if (PosicionAterrizaje != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(PosicionAterrizaje);
      }
      if (AnteriorAterrizaje.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(AnteriorAterrizaje);
      }
      if (IdAvion.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(IdAvion);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(Resp_At other) {
      if (other == null) {
        return;
      }
      if (other.AutorizacionAterrizaje != false) {
        AutorizacionAterrizaje = other.AutorizacionAterrizaje;
      }
      if (other.PistaAterrizaje != 0) {
        PistaAterrizaje = other.PistaAterrizaje;
      }
      if (other.AlturaAterrizaje != 0) {
        AlturaAterrizaje = other.AlturaAterrizaje;
      }
      if (other.PosicionAterrizaje != 0) {
        PosicionAterrizaje = other.PosicionAterrizaje;
      }
      if (other.AnteriorAterrizaje.Length != 0) {
        AnteriorAterrizaje = other.AnteriorAterrizaje;
      }
      if (other.IdAvion.Length != 0) {
        IdAvion = other.IdAvion;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 8: {
            AutorizacionAterrizaje = input.ReadBool();
            break;
          }
          case 16: {
            PistaAterrizaje = input.ReadInt32();
            break;
          }
          case 24: {
            AlturaAterrizaje = input.ReadInt32();
            break;
          }
          case 32: {
            PosicionAterrizaje = input.ReadInt32();
            break;
          }
          case 42: {
            AnteriorAterrizaje = input.ReadString();
            break;
          }
          case 50: {
            IdAvion = input.ReadString();
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code