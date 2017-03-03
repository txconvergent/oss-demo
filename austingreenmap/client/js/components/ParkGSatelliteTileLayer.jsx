import {TileLayer} from "react-leaflet";

export default class ParkGSatelliteTileLayer extends TileLayer  {
  componentWillMount() {

    this.props.url = 'http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}&s=Ga';
    this.props.attribution = '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>';

    super.componentWillMount();
  }
}

ParkGSatelliteTileLayer.propTypes = {};
