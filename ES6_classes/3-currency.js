export default class Currency {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  set name(value) {
    this._name = this.name;
  }

  set code(value) {
    this._code = this.code;
  }


  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}