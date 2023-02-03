// Monthly Average Shares
import java.util.*;
import java.io.IOException;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class fbs
{
	public static class fbsMapper extends MapReduceBase implements
	Mapper <Object ,/*Input Key Type */
	Text, /*input value type*/
	IntWritable, /*Output key type*/
	IntWritable> /*Output value Type*/
	{
	// Map Function
	boolean flag = false;
	public void map(Object key, Text value, OutputCollector<IntWritable, IntWritable> output, Reporter reporter) throws    													IOException 
	   {
		String line[] = value.toString().split(",",20);
		if(flag)
		{
			String date = line[2];
			int shares = Integer.parseInt(line[5]);
			  if(date.contains("2017"))
			  {
			   	String x[] = date.split("/",3);
			   	int month = Integer.parseInt(x[0]); 
			  	output.collect(new IntWritable(month),new IntWritable(shares));     
			  }
			  
		}
	          flag = true;
	   }
	}
	
	//Reducer class
	public static class fbsReducer extends MapReduceBase implements 
	Reducer< IntWritable, IntWritable, IntWritable, FloatWritable > 
	{
		//Reduce function 
		public void reduce(IntWritable key,Iterator <IntWritable> values,OutputCollector<IntWritable, FloatWritable>    											output,Reporter reporter) throws IOException
		{
			int add = 0, total=0;
			while(values.hasNext())
			{
				add = add + values.next().get();	
				total++;
			}
			output.collect(key, new FloatWritable(add/(float)total));
		}
	
	}


	  //Main function 
          public static void main(String args[]) throws Exception
          {
		JobConf conf = new JobConf(fbs.class);
		conf.setJobName("Facebook Share");
		conf.setOutputKeyClass(IntWritable.class);
		conf.setOutputValueClass(FloatWritable.class);
		conf.setMapOutputKeyClass(IntWritable.class);
		conf.setMapOutputValueClass(IntWritable.class);
		conf.setMapperClass(fbsMapper.class);
		conf.setReducerClass(fbsReducer.class);
		conf.setInputFormat(TextInputFormat.class);
		conf.setOutputFormat(TextOutputFormat.class);
		FileInputFormat.setInputPaths(conf, new Path(args[0]));
		FileOutputFormat.setOutputPath(conf, new Path(args[1]));
		JobClient.runJob(conf);
	  }
}


