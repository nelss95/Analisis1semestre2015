/**
 * Created by nelson on 23/05/15.
 */
public class Actividad {
    String nombre;
    int horaInicio;
    int horaFinal;
    int tiempoActividad;


    byte [] genes;

    public Actividad(String nombre, int horaInicio, int horaFinal, int tiempoActividad, byte[] genes) {
        this.nombre = nombre;
        this.horaInicio = horaInicio;
        this.horaFinal = horaFinal;
        this.tiempoActividad = tiempoActividad;
        this.genes = genes;
    }





    public int getHoraInicio() {
        return horaInicio;
    }

    public void setHoraInicio(int horaInicio) {
        this.horaInicio = horaInicio;
    }

    public int getHoraFinal() {
        return horaFinal;
    }

    public void setHoraFinal(int horaFinal) {
        this.horaFinal = horaFinal;
    }

    public int getTiempoActividad() {
        return tiempoActividad;
    }

    public void setTiempoActividad(int tiempoActividad) {
        this.tiempoActividad = tiempoActividad;
    }

    public byte[] getGenes() {
        return genes;
    }

    public void setGenes(byte[] genes) {
        this.genes = genes;
    }


}
