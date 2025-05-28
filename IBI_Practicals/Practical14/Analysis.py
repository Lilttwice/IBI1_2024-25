# Libraries needed for XML parsing and performance measurement
import xml.dom.minidom
import xml.sax
import time
import os
from datetime import datetime

# Configuration
XML_FILE = 'go_obo.xml'
NAMESPACES = {
    "molecular_function": {"max_count": 0, "terms": []},
    "biological_process": {"max_count": 0, "terms": []},
    "cellular_component": {"max_count": 0, "terms": []}
}

# DOM Parser Implementation
# 1. Load XML file using DOM parser
# 2. For each <term> element:
#    - Extract ID, name, and namespace
#    - Count number of <is_a> child elements
#    - Track maximum is_a count per namespace
#    - Update list of terms with maximum count
# 3. Print results for each namespace
# 4. Measure and return execution time

def parse_with_dom(file_path):
    """Parse GO terms using DOM API and track max is_a counts per namespace"""
    print("\n=== DOM Parser Analysis ===")
    start_time = time.perf_counter()
    
    try:
        # Parse XML into DOM tree
        doc = xml.dom.minidom.parse(file_path)
        terms = doc.getElementsByTagName("term")
        
        # Initialize tracking structure
        namespace_stats = {ns: {"max_count": 0, "terms": []} for ns in NAMESPACES}
        
        # Process each term element
        for term in terms:
            # Extract term metadata
            term_id = term.getElementsByTagName("id")[0].firstChild.data.strip()
            term_name = term.getElementsByTagName("name")[0].firstChild.data.strip()
            namespace = term.getElementsByTagName("namespace")[0].firstChild.data.strip()
            
            # Skip irrelevant namespaces
            if namespace not in namespace_stats:
                continue
                
            # Count is_a relationships
            is_a_elements = term.getElementsByTagName("is_a")
            is_a_count = len(is_a_elements)
            
            # Update maximum count tracking
            current_max = namespace_stats[namespace]["max_count"]
            if is_a_count > current_max:
                namespace_stats[namespace] = {"max_count": is_a_count, "terms": [(term_id, term_name)]}
            elif is_a_count == current_max:
                namespace_stats[namespace]["terms"].append((term_id, term_name))
        
        # Format and print results
        _print_results(namespace_stats)
        
    except Exception as e:
        print(f"Error during DOM parsing: {e}")
        return None
    
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"DOM Parsing Time: {duration:.4f} seconds")
    return duration

# SAX Parser Implementation
# 1. Create SAX content handler class
# 2. On start of <term> element:
#    - Reset tracking variables
# 3. On start of <is_a> element:
#    - Increment is_a counter
# 4. On text content:
#    - Collect ID, name, namespace values
# 5. On end of <term> element:
#    - Update maximum is_a count tracking
# 6. Configure and run SAX parser
# 7. Print results for each namespace
# 8. Measure and return execution time

def parse_with_sax(file_path):
    """Parse GO terms using SAX API and track max is_a counts per namespace"""
    print("\n=== SAX Parser Analysis ===")
    start_time = time.perf_counter()
    
    class GOTermHandler(xml.sax.ContentHandler):
        def __init__(self):
            # Initialize tracking variables
            self.current_element = ""
            self.current_id = ""
            self.current_name = ""
            self.current_namespace = ""
            self.is_a_count = 0
            self.namespace_stats = {ns: {"max_count": 0, "terms": []} for ns in NAMESPACES}
            
        def startElement(self, name, attrs):
            # Handle start of XML elements
            self.current_element = name
            if name == "term":
                # Reset term-specific variables
                self.current_id = ""
                self.current_name = ""
                self.current_namespace = ""
                self.is_a_count = 0
            elif name == "is_a":
                # Count is_a relationships
                self.is_a_count += 1
                
        def characters(self, content):
            # Collect text content for relevant elements
            if self.current_element == "id":
                self.current_id += content.strip()
            elif self.current_element == "name":
                self.current_name += content.strip()
            elif self.current_element == "namespace":
                self.current_namespace += content.strip()
                
        def endElement(self, name):
            # Process completed elements
            if name == "term":
                # Update statistics if namespace is relevant
                if self.current_namespace in self.namespace_stats:
                    current_max = self.namespace_stats[self.current_namespace]["max_count"]
                    if self.is_a_count > current_max:
                        self.namespace_stats[self.current_namespace] = {
                            "max_count": self.is_a_count,
                            "terms": [(self.current_id, self.current_name)]
                        }
                    elif self.is_a_count == current_max:
                        self.namespace_stats[self.current_namespace]["terms"].append(
                            (self.current_id, self.current_name)
                        )
                self.current_element = ""
                
    try:
        # Configure and run SAX parser
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        handler = GOTermHandler()
        parser.setContentHandler(handler)
        parser.parse(file_path)
        
        # Format and print results
        _print_results(handler.namespace_stats)
        
    except Exception as e:
        print(f"Error during SAX parsing: {e}")
        return None
    
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"SAX Parsing Time: {duration:.4f} seconds")
    return duration

# Helper Function for Result Display
# 1. For each namespace:
#    - Check if terms exist
#    - Format and print maximum count
#    - Format and print all terms with maximum count

def _print_results(stats):
    """Helper function to format and print results"""
    for namespace, data in stats.items():
        max_count = data["max_count"]
        terms = data["terms"]
        
        if not terms:
            print(f"Namespace: {namespace} - No terms found")
            continue
            
        term_info = []
        for term_id, term_name in terms:
            term_info.append(f"ID={term_id}, GO{term_id[3:]}, Name={term_name}")
            
        print(f"Namespace: {namespace}")
        print(f"  Max is_a count: {max_count}")
        print(f"  Terms: {', '.join(term_info)}\n")

# Main Program Execution
# 1. Print start time and file information
# 2. Check if XML file exists
# 3. Run DOM parser and record execution time
# 4. Run SAX parser and record execution time
# 5. Compare execution times and print results

def main():
    """Main execution function"""
    print(f"Analysis Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Processing file: {XML_FILE}\n")
    
    # Validate file existence
    if not os.path.exists(XML_FILE):
        print(f"Error: File {XML_FILE} not found!")
        return
    
    # Run both parsers and compare performance
    dom_time = parse_with_dom(XML_FILE)
    sax_time = parse_with_sax(XML_FILE)
    
    if dom_time and sax_time:
        print("\n=== Performance Comparison ===")
        if dom_time < sax_time:
            print(f"DOM parser is faster by {sax_time - dom_time:.4f} seconds")
        elif sax_time < dom_time:
            print(f"SAX parser is faster by {dom_time - sax_time:.4f} seconds")
        else:
            print("Both parsers took the same amount of time")
        
        print(f"Speed difference ratio: {max(dom_time, sax_time)/min(dom_time, sax_time):.2f}x")

if __name__ == "__main__":
    main()