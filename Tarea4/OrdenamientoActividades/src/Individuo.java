
public class Individuo {

    static int largoDeGenesPorDefecto = 8;
    private byte[] genes = new byte[largoDeGenesPorDefecto];
    private Actividad[] cronograma = new Actividad[largoDeGenesPorDefecto];
    // Cache
    private int fitness = 0;


    // crea un Individuo al azar
    public void generarIndividuo() {
        for (int i = 0; i < tamanno(); i++) {
            byte gen = (byte) Math.round(Math.random());
            genes[i] = gen;
        }

        for (int i = 0; i < tamanno(); i++) {
            int horaInicio = (int) Math.floor(Math.random()*24);
            int horaFinal = (int) Math.floor(Math.random()*24);
            Actividad cro = new Actividad("Concierto "+i,horaInicio,horaFinal,horaFinal-horaInicio,genes);
            cronograma[i] = cro;
        }
    }


    // Utilice esto para cambiar el largo de los genes
    public static void establecerLargoDeGenesPorDefecto(int largo) {
        largoDeGenesPorDefecto = largo;
    }
    
    public byte obtenerGen(int index) {
        return cronograma[index].genes[index];
    }

    public void establecerGen(int index, byte valor) {
        cronograma[index].genes[index] = valor;
        fitness = 0;
    }

    public int tamanno() {
        return cronograma.length;
    }

    public int obtenerFitness() {
        if (fitness == 0) {
            fitness = FuncionDeFitness.obtenerFitness(this);
        }
        return fitness;
    }

    @Override
    public String toString() {
        String stringDeGenes = "";
        for (int i = 0; i < tamanno(); i++) {
            stringDeGenes += obtenerGen(i);
        }
        return stringDeGenes;
    }
}